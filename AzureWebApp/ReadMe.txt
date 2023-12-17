#Deploy a Python (Flask) web app in Azure

#Get python flast based sample app code
    git clone https://github.com/Azure-Samples/msdocs-python-flask-webapp-quickstart

#Create a virtual environment for the app:
    python3 -m venv .venv
    source .venv/bin/activate

#Install the dependencies:
    pip install -r requirements.txt

#Create the webapp and other resources, then deploy your code to Azure using az webapp up.

    az webapp up --runtime PYTHON:3.9 --sku F1 --logs --name PyAzure3WebApp --location eastus

    ebapp 'PyAzure3WebApp' already exists. The command will deploy contents to the existing app.
    Creating AppServicePlan 'pawgupta0_asp_8580' ...
    Updating runtime version from PYTHON|3.11 to PYTHON|3.9
    Waiting for runtime version to propagate ...
    Creating zip with contents of dir /Users/pawgupta0/Pawanesh/development/AzureCloud/AzureWebApp/msdocs-python-flask-webapp-quickstart ...
    Getting scm site credentials for zip deployment
    Starting zip deployment. This operation can take a while to complete ...
    Deployment endpoint responded with status code 202
    You can launch the app at http://pyazure3webapp.azurewebsites.net
    Configuring default logging for the app, if not already enabled
    2023-08-29T18:00:36  Welcome, you are now connected to log-streaming service.


#First, you need to configure Azure App Service to output logs to the App Service filesystem using the az webapp log config command.

    az webapp log config \
    --web-server-logging filesystem \
    --name PyAzure3WebApp \
    --resource-group pawgupta0_rg_9796


                   az webapp log config \
                    >     --web-server-logging filesystem \
                    >     --name PyAzure3WebApp \
                    >     --resource-group pawgupta0_rg_9796
                    {
                    "applicationLogs": {
                        "azureBlobStorage": {
                        "level": "Off",
                        "retentionInDays": null,
                        "sasUrl": null
                        },
                        "azureTableStorage": {
                        "level": "Off",
                        "sasUrl": null
                        },
                        "fileSystem": {
                        "level": "Off"
                        }
                    },
                    "detailedErrorMessages": {
                        "enabled": false
                    },
                    "failedRequestsTracing": {
                        "enabled": false
                    },
                    "httpLogs": {
                        "azureBlobStorage": {
                        "enabled": false,
                        "retentionInDays": 3,
                        "sasUrl": null
                        },
                        "fileSystem": {
                        "enabled": true,
                        "retentionInDays": 3,
                        "retentionInMb": 100
                        }
                    },
                    "id": "/subscriptions/17e6b87f-6549-4a64-91e0-dbda9e0d5be2/resourceGroups/pawgupta0_rg_9796/providers/Microsoft.Web/sites/PyAzure3WebApp/config/logs",
                    "kind": null,
                    "location": "East US",
                    "name": "logs",
                    "resourceGroup": "pawgupta0_rg_9796",
                    "type": "Microsoft.Web/sites/config"
                    }


#To stream logs, use the az webapp log tail command.

    az webapp log tail \
    --name PyAzure3WebApp \
    --resource-group pawgupta0_rg_9796

#Clean up
    az group delete --name pawgupta0_rg_9796  
    Are you sure you want to perform this operation? (y/n): y





----------------------------------------------------------------------------------------
#Deploy a Python (Django or Flask) web app with PostgreSQL in Azure



-----------------------------------------------------------------------------------------
#Create a static HTML web app by using Azure Cloud Shell

#Clone the code from git
        mkdir htmlapp

        cd htmlapp

        git clone https://github.com/Azure-Samples/html-docs-hello-world.git

#Ceate resource group
        bash-3.2$ az group create --name webapp-rg --location eastus
        {
        "id": "/subscriptions/17e6b87f-6549-4a64-91e0-dbda9e0d5be2/resourceGroups/webapp-rg",
        "location": "eastus",
        "managedBy": null,
        "name": "webapp-rg",
        "properties": {
            "provisioningState": "Succeeded"
        },
        "tags": null,
        "type": "Microsoft.Resources/resourceGroups"
        }
        bash-3.2$ az group list -o table
        Name                      Location    Status
        ------------------------  ----------  ---------
        NetworkWatcherRG          eastus      Succeeded
        DefaultResourceGroup-EUS  eastus      Succeeded
        webapp-rg                 eastus      Succeeded



#Create the web app

            cd html-docs-hello-world

            az webapp up -g webapp-rg -n static-web-app-101 --html
            The webapp 'static-web-app-101' doesn't exist
            Creating AppServicePlan 'pawgupta0_asp_2388' ...
            Creating webapp 'static-web-app-101' ...
            Configuring default logging for the app, if not already enabled
            Creating zip with contents of dir /Users/pawgupta0/Pawanesh/development/AzureCloud/AzureWebApp/htmlapp/html-docs-hello-world ...
            Getting scm site credentials for zip deployment
            Starting zip deployment. This operation can take a while to complete ...
            Deployment endpoint responded with status code 202
            You can launch the app at http://static-web-app-101.azurewebsites.net
            Setting 'az webapp up' default arguments for current directory. Manage defaults with 'az configure --scope local'
            --resource-group/-g default: webapp-rg
            --sku default: F1
            --plan/-p default: pawgupta0_asp_2388
            --location/-l default: eastus
            --name/-n default: static-web-app-101
            {
            "URL": "http://static-web-app-101.azurewebsites.net",
            "appserviceplan": "pawgupta0_asp_2388",
            "location": "eastus",
            "name": "static-web-app-101",
            "os": "Windows",
            "resourcegroup": "webapp-rg",
            "runtime_version": "-",
            "runtime_version_detected": "-",
            "sku": "FREE",
            "src_path": "//Users//pawgupta0//Pawanesh//development//AzureCloud//AzureWebApp//htmlapp//html-docs-hello-world"
            }


#Change coode and redeploy the web app 

            bash-3.2$ vim index.html (In the <h1> heading tag, change Azure App Service - Sample Static HTML Site to Azure App Service Updated - or to anything else that you'd like.)
)
            bash-3.2$ az webapp up -g webapp-rg -n static-web-app-101 --html
            Webapp 'static-web-app-101' already exists. The command will deploy contents to the existing app.
            Creating AppServicePlan 'pawgupta0_asp_2388' ...
            Creating zip with contents of dir /Users/pawgupta0/Pawanesh/development/AzureCloud/AzureWebApp/htmlapp/html-docs-hello-world ...
            Getting scm site credentials for zip deployment
            Starting zip deployment. This operation can take a while to complete ...
            Deployment endpoint responded with status code 202
            You can launch the app at http://static-web-app-101.azurewebsites.net
            Setting 'az webapp up' default arguments for current directory. Manage defaults with 'az configure --scope local'
            --resource-group/-g default: webapp-rg
            --sku default: F1
            --plan/-p default: pawgupta0_asp_2388
            --location/-l default: eastus
            --name/-n default: static-web-app-101
            {
            "URL": "http://static-web-app-101.azurewebsites.net",
            "appserviceplan": "pawgupta0_asp_2388",
            "location": "eastus",
            "name": "static-web-app-101",
            "os": "Windows",
            "resourcegroup": "webapp-rg",
            "runtime_version": "-",
            "runtime_version_detected": "-",
            "sku": "FREE",
            "src_path": "//Users//pawgupta0//Pawanesh//development//AzureCloud//AzureWebApp//htmlapp//html-docs-hello-world"
            }


#Cleanup
    az group delete --name webapp-rg
    Are you sure you want to perform this opera
    

az webapp log config \
    --web-server-logging filesystem \
    --name test-webapp-pg230 \
    --resource-group test-webapp-rg

az webapp log tail \
    --name test-webapp-pg230 \
    --resource-group test-webapp-rg



az webapp log download --resource-group test-webapp-rg  --name test-webapp-pg230 --log-file ftp://waws-prod-blu-353.ftp.azurewebsites.windows.net/site/wwwroot


#Web app deploy using cli
    az group create --name webapp-cli-rg --location eastus
    az appservice plan create --name webappcliplan-1 -g webapp-cli-rg --location eastus --sku B1 --is-linux
    az webapp create -g webapp-cli-rg -p webappcliplan-1 -n webappclipg230 --runtime "PYTHON:3.11" 
    az webapp deploy -g webapp-cli-rg --name webappclipg230 --src-path /Users/pawgupta0/Pawanesh/development/AzureCloud/AzureWebAppCLI/Archive.zip --type zip              
