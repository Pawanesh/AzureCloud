# Login
    az login


#Next, install the Azure Container Apps extension for the CLI.
    az extension add --name containerapp --upgrade

#Now that the current extension or module is installed, register the Microsoft.App namespace.
    az provider register --namespace Microsoft.App


#Register the Microsoft.OperationalInsights provider for the Azure Monitor Log Analytics workspace if you have not used it before.
    az provider register --namespace Microsoft.OperationalInsights



#Set resuable environmentVariables
    LOCATION="eastus"
    RESOURCE_GROUP="my-container-apps-rg"
    CONTAINERAPP_ENVIRONMENT="my-container-apps-env"

#Create resource group
    az group create --name $RESOURCE_GROUP --location $LOCATION

#Create container app environment
    az containerapp env create --name $CONTAINERAPP_ENVIRONMENT --resource-group $RESOURCE_GROUP --location $LOCATION