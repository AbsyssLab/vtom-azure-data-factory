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
  * Creation of a virtual environment (venv):
    
    Go to the project directory (which contains the scripts and the requirements.txt file):
    * python → your interpreter
    * .venv → the folder that will contain the virtual environment (best practice: always inside the project repository).

    From the command line (Windows or Linux):
    ```bash
    python -m venv .venv
    ```
    
    This creates the following structure:
    
    my_project/
    * .venv/       <- vitual environment
    * azureDataFactory.py
    * requirements.txt

  * Activating the virtual environment :

     On Windows :
     ```
     my_project\.venv\Scripts\activate.bat
     ```
     On Linux :
     ```
     source my_project/.venv/bin/activate
     ```
    When activated, the command prompt usually displays (venv) or (.venv) → all pip install commands will install packages inside this environment.

    Install the required Python packages in your virtual environment:
    ```
    pip install -r requirements.txt
    ```

 * Installation and configuration of Windows and Linux queues :
    * Unix Agent : tom_submit.azdatafactory
    * Windows Agent : submit_queue_azdatafactory.bat 
  
  Set the PROJECT_PATH variable in the batch queue (Windows or Linux) to indicate your project directory.
  
  Examples : 
  ```
  set PROJECT_PATH=%TOM_HOME%\SCRIPTS\AzureDataFactory\
  ```
  or
  ```
 project_path=/var/lib/absyss/visual-tom/scripts/azure/az-datafactory
  ```
# Instructions

  * Create an Azure Application and set the following environment variables in a object Context Visual TOM :
    * `AZURE_SUBSCRIPTION_ID`: Subscription ID of your Azure subscription
    * `AZURE_TENANT_ID`: Tenant ID of your Azure Active Directory
    * `AZURE_CLIENT_ID`: Client ID of your Azure Active Directory application
    * `AZURE_CLIENT_SECRET`: Client secret of your Azure Active Directory application
    * `AZURE_DATA_FACTORY_RESOURCE_GROUP`: Resource group of your Azure Data Factory
      
  Resources Secret are recommanded :

  ![Custom application screenshot](screenshots/AzureDataFactory_Context.png?raw=true)
  * Create in Visual TOM a "Custom Application" connection with the following definition or import the file MyApplication-AzureDataFactory.xml:
  ```bash
  vtimport -x -f MyApplication-AzureDataFactory.xml
  ```
  ![Custom application screenshot](screenshots/AzureDataFactory_CustomApp_WebInterface.png?raw=true)
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
