brew tap azure/functions

brew install azure-functions-core-tools@4

python -m venv .venv

source .venv/bin/activate

func init LocalFunctionProj --python -m V2

cd LocalFunctionProj/


ls -ltr
    total 32
    -rw-r--r--  1 pawgupta0  staff  203 Sep  1 10:59 requirements.txt
    -rw-r--r--  1 pawgupta0  staff   71 Sep  1 10:59 function_app.py
    -rw-r--r--  1 pawgupta0  staff  288 Sep  1 10:59 host.json
    -rw-r--r--  1 pawgupta0  staff  173 Sep  1 10:59 local.settings.json


cat requirements.txt
    # Do not include azure-functions-worker in this file
    # The Python Worker is managed by the Azure Functions platform
    # Manually managing azure-functions-worker may cause unexpected issues

    azure-functions


cat function_app.py
    import azure.functions as func

    app = func.FunctionApp()

    @app.function_name(name="HttpExample")
    @app.route(route="hello")
    def test_function(req: func.HttpRequest) -> func.HttpResponse:
        return func.HttpResponse("HttpExample function processed a request!")


cat host.json
    {
    "version": "2.0",
    "logging": {
        "applicationInsights": {
        "samplingSettings": {
            "isEnabled": true,
            "excludedTypes": "Request"
        }
        }
    },
    "extensionBundle": {
        "id": "Microsoft.Azure.Functions.ExtensionBundle",
        "version": "[4.*, 5.0.0)"
    }
    }


cat local.settings.json
    {
    "IsEncrypted": false,
    "Values": {
        "FUNCTIONS_WORKER_RUNTIME": "python",
        "AzureWebJobsFeatureFlags": "EnableWorkerIndexing",
        "AzureWebJobsStorage": "UseDevelopmentStorage=true"
    }
    }




func start
    Found Python version 3.9.13 (python3).

    Azure Functions Core Tools
    Core Tools Version:       4.0.5312 Commit hash: N/A  (64-bit)
    Function Runtime Version: 4.23.2.21220

    [2023-09-01T15:17:36.361Z] Worker process started and initialized.

    Functions:

        HttpExample:  http://localhost:7071/api/hello









az group create --name AzureFunctionsQuickstart-rg --location eastus

az storage account create --name functionappstorage101  --location eastus --resource-group AzureFunctionsQuickstart-rg --sku Standard_LRS

az functionapp create --resource-group AzureFunctionsQuickstart-rg --consumption-plan-location eastus --runtime python --runtime-version 3.9 --functions-version 4 --name PyFunctionApp101 --os-type linux --storage-account functionappstorage101


func azure functionapp publish PyFunctionApp101


az functionapp config appsettings set --name PyFunctionApp101  --resource-group AzureFunctionsQuickstart-rg  --settings AzureWebJobsFeatureFlags=EnableWorkerIndexing


func azure functionapp logstream PyFunctionApp101 --browser



