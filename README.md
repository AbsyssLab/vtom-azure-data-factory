# Azure Data Factory integration
[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](LICENSE.md)&nbsp;
[![fr](https://img.shields.io/badge/lang-fr-yellow.svg)](README-fr.md)  

This integration allows to trigger and monitor Azure Data Factory pipelines from Visual TOM.

# Disclaimer
No Support and No Warranty are provided by Absyss SAS for this project and related material. The use of this project's files is at your own risk.

Absyss SAS assumes no liability for damage caused by the usage of any of the files offered here via this Github repository.

Consultings days can be requested to help for the implementation.

# Prerequisites

  * Visual TOM 7.1.2 or greater
  * Python 3.x or greater
  * Azure Data Factory resource
  * Install the required python packages using pip:
    ```bash
    pip install -r requirements.txt
    ```
  * Unix Agent (Windows usage will be available later)

# Instructions

  * Create an Azure Application and set the following environment variables in config.py in the same folder (a template is available in the repository):
    * `AZURE_SUBSCRIPTION_ID`: Subscription ID of your Azure subscription
    * `AZURE_TENANT_ID`: Tenant ID of your Azure Active Directory
    * `AZURE_CLIENT_ID`: Client ID of your Azure Active Directory application
    * `AZURE_CLIENT_SECRET`: Client secret of your Azure Active Directory application
    * `AZURE_DATA_FACTORY_RESOURCE_GROUP`: Resource group of your Azure Data Factory
  * Create in Visual TOM a "Custom Application" connection with the following definition or import the file MyApplication-AzureDataFactory.xml:
  ```bash
  vtimport -x -f MyApplication-AzureDataFactory.xml
  ```
  ![Custom application screenshot](screenshots/Azure_DataFactory_CustomApplication.png?raw=true)
  * Create the batch queue on the Agents and update the submitter with actual path of azureDataFactory.py

Description of the parameters:
  * Data Factory: Name of the Data Factory
  * Pipeline: Name of the pipeline to trigger
  * Parameters (optional): JSON file or short JSON string of the parameters to pass to the pipeline
    * In case of JSON string, the parameter must start with "E<>|" to avoid "Resource not found" error

The integration returns specific codes for errors:
  * 90: Inconsistent parameters
  * 99: Activity failed or cancelled

# License
This project is licensed under the Apache 2.0 License - see the [LICENSE](license) file for details


# Code of Conduct
[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-v2.1%20adopted-ff69b4.svg)](code-of-conduct.md)  
Absyss SAS has adopted the [Contributor Covenant](CODE_OF_CONDUCT.md) as its Code of Conduct, and we expect project participants to adhere to it. Please read the [full text](CODE_OF_CONDUCT.md) so that you can understand what actions will and will not be tolerated.
