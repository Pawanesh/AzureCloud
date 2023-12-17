#Create resource group
    az group create --name func-binding-rg --location eastus


#Create storage account
    az storage account create --name funcbindstorage --location eastus --resource-group func-binding-rg --sku Standard_LRS

    Key1: vOLupUWhyEtZuR6iGkD3fCbOVnujs8Oqobq6jHrB6Iogr6+E5mYfQwGYbHTHEc44jwgo2hZQNLGX+AStgiiHnw==

    ConnStr1: DefaultEndpointsProtocol=https;AccountName=funcbindstorage;AccountKey=vOLupUWhyEtZuR6iGkD3fCbOVnujs8Oqobq6jHrB6Iogr6+E5mYfQwGYbHTHEc44jwgo2hZQNLGX+AStgiiHnw==;EndpointSuffix=core.windows.net

#Create container inputbinding in storage account
    az storage container create --name inputbinding --account-name funcbindstorage


#Create container outbinding in storage account
    az storage container create --name outputbinding --account-name funcbindstorage


#Create appservice plan 
    az appservice plan create --name bindingappplan --is-linux --sku b1 -g func-binding-rg

#Create functionapp
    az functionapp create --name bindingfuncapp -g func-binding-rg --os-type Linux --runtime Python --storage-account funcbindstorage -p bindingappplan --runtime-version 3.9 --functions-version 4

#Deploye code
    func azure functionapp publish bindingfuncapp

    az functionapp config appsettings set --name bindingfuncapp  --resource-group func-binding-rg   --settings AzureWebJobsFeatureFlags=EnableWorkerIndexing
