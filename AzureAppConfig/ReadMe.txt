#Create resource group
    az group create --name app-config-resource --location eastus

#Create an App Configuration store
    az appconfig create --name app-config-dev-pg --resource-group app-config-resource --location eastus

#Create a key-value
    az appconfig kv set --name app-config-dev-pg --key Send:Email --value pawaneshg@gmail.com

@Create a feature flag
    az appconfig feature set --name app-config-dev-pg --feature featureA

#Create python venv and activate
    python -m venv .venv
    source .venv/bin/activate

#Install azure app config python pkg
    pip install azure-appconfiguration-provider

#Test appconfig
    export AZURE_APPCONFIG_CONNECTION_STRING='Endpoint=https://app-config-dev-pg.azconfig.io;Id=t3Sk;Secret=DVY8OCtzrB+sHVqn8GLwn+nPAwF+sLAnk41pvLPGxN4='

    (.venv) (base) pawgupta0@WKMZT1D2F51B AzureAppConfig % 
    python app-configuration-quickstart.py 
    Hello
    value
    Hello test
    message found: True
    test.message found: False

#Reference
    https://learn.microsoft.com/en-us/azure/azure-app-configuration/quickstart-python-provider?tabs=linux%2Cflask
