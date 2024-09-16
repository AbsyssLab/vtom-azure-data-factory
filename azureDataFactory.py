from azure.identity import ClientSecretCredential
from azure.mgmt.datafactory import DataFactoryManagementClient
import time
import argparse
import json
import os
from config import *

#####################################################
### Function to print messages to the standard output
#####################################################
def printFormat(typeMessage: str, Content:str):
	timestamp=(time.strftime("%H:%M:%S", time.localtime()))
	print(timestamp + ' | ' + typeMessage.ljust(7) + ' | ' + Content)
	return;

#####################################################
### Managing parameters (JSON string or file path)
#####################################################
def load_json_param(param):
    if param is None:
        return {}
    if os.path.isfile(param):
        with open(param, 'r') as f:
            return json.load(f)
    else:
        try:
            return json.loads(param)
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON string or file path provided")

# Argument parsing
parser = argparse.ArgumentParser(description='Trigger and monitor an Azure Data Factory pipeline.')
parser.add_argument('--factory', type=str, required=True, help='Name of the Azure Data Factory')
parser.add_argument('--pipeline', type=str, required=True, help='Name of the pipeline to run')
parser.add_argument('--params', type=str, help='JSON string or path to JSON file containing pipeline parameters')
args = parser.parse_args()

# Configuration
factory_name = args.factory
pipeline_name = args.pipeline
pipeline_params = load_json_param(args.params)
sleep_time = 30

printFormat("INFO", f"Arguments:")
printFormat("INFO", f"  - Factory name: {factory_name}")
printFormat("INFO", f"  - Pipeline name: {pipeline_name}")
printFormat("INFO", f"  - Pipeline parameters:")
print(json.dumps(pipeline_params, indent=4))
print("")
# Authentication
token_credential = ClientSecretCredential(AZURE_TENANT_ID, AZURE_CLIENT_ID, AZURE_CLIENT_SECRET)


# Create Data Factory client
printFormat("INFO", f"Creating Data Factory client")
adf_client = DataFactoryManagementClient(token_credential, AZURE_SUBSCRIPTION_ID)

# Trigger the pipeline
printFormat("INFO", f"Triggering pipeline")
run_response = adf_client.pipelines.create_run(AZURE_DATA_FACTORY_RESOURCE_GROUP, factory_name, pipeline_name, parameters=pipeline_params)

# Follow up on the execution
while True:
    printFormat("INFO", f"Getting pipeline run status (every {sleep_time} seconds)")
    pipeline_run = adf_client.pipeline_runs.get(AZURE_DATA_FACTORY_RESOURCE_GROUP, factory_name, run_response.run_id)
    printFormat("INFO", f"Status: {pipeline_run.status}")
    
    if pipeline_run.status in ["Succeeded", "Failed", "Cancelled"]:
        break
    
    time.sleep(sleep_time)  # Wait for 30 seconds before the next check

# Display logs
activity_runs = adf_client.activity_runs.query_by_pipeline_run(
    AZURE_DATA_FACTORY_RESOURCE_GROUP,
    factory_name,
    run_response.run_id,
    {
        "lastUpdatedAfter": pipeline_run.run_start,
        "lastUpdatedBefore": pipeline_run.run_end
    }
)

print("")
for activity_run in activity_runs.value:
    printFormat("INFO", f"Activity: {activity_run.activity_name}")
    printFormat("INFO", f"Status: {activity_run.status}")

if activity_run.status in ["Failed", "Cancelled"]:
    printFormat("ERROR", f"Activity {activity_run.activity_name} failed with error: {json.dumps(activity_run.error, indent=4)}")
    exit(99)