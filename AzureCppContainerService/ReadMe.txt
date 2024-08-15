https://medium.com/@ngerakines/dipping-a-toe-into-cpprestsdk-a40b063fe3f5

## Build app image and test locally
    docker build . -t "cpp-test-app-image:v1.0" -f ./Dockerfile

    docker run --rm -p 8080:8080 cpp-test-app-image:v1.0

## Create ACR
    az login

    az group create --name omm-acr-rg --location eastus

    az acr create --resource-group omm-acr-rg --name ommazurecontainerregistry --sku Basic 

    base) pawgupta0@WKMZT1D2F51B ~ % az acr list -o table -g omm-acr-rg
    NAME                       RESOURCE GROUP    LOCATION    SKU    LOGIN SERVER                          CREATION DATE         ADMIN ENABLED
    -------------------------  ----------------  ----------  -----  ------------------------------------  --------------------  ---------------
    ommazurecontainerregistry  omm-acr-rg        eastus      Basic  ommazurecontainerregistry.azurecr.io  2024-04-08T20:37:03Z  False

## Push image to acr
    az acr login --name ommazurecontainerregistry

    docker tag  cpp-test-app-image:v1.0 ommazurecontainerregistry.azurecr.io/cpp-test-app-image ommazurecontainerregistry.azurecr.io/cpp-test-app-image 

    docker push ommazurecontainerregistry.azurecr.io/cpp-test-app-image 


    az acr list -o table
    NAME                       RESOURCE GROUP    LOCATION    SKU    LOGIN SERVER                          CREATION DATE         ADMIN ENABLED
    -------------------------  ----------------  ----------  -----  ------------------------------------  --------------------  ---------------
    ommazurecontainerregistry  omm-acr-rg        eastus      Basic  ommazurecontainerregistry.azurecr.io  2024-04-08T20:37:03Z  False


    az acr repository list --name ommazurecontainerregistry -o table
    Result
    ------------------
    cpp-test-app-image


## Create container app using image in acr

    az group create --location eastus --resource-group cpp-test-container-apps

    az acr login --name ommazurecontainerregistry
    
    az containerapp up --name cpp-test-container-app --resource-group cpp-test-container-apps --location eastus --environment 'cpp-test-container-apps-env' --image ommazurecontainerregistry.azurecr.io/cpp-test-app-image --target-port 8080 --ingress external --query properties.configuration.ingress.fqdn

    sing resource group 'cpp-test-container-apps'
    Creating ContainerAppEnvironment 'cpp-test-container-apps-env' in resource group cpp-test-container-apps
    No Log Analytics workspace provided.
    Generating a Log Analytics workspace with name "workspace-cpptestcontainerappsnNlD"
    Creating Containerapp cpp-test-container-app in resource group cpp-test-container-apps
    Adding registry password as a secret with name "ommazurecontainerregistryazurecrio-ommazurecontainerregistry"

    Container app created. Access your app at https://cpp-test-container-app.whitedesert-6cef983a.eastus.azurecontainerapps.io/


    Your container app cpp-test-container-app has been created and deployed! Congrats! 

    Browse to your container app at: http://cpp-test-container-app.whitedesert-6cef983a.eastus.azurecontainerapps.io 

    Stream logs for your container with: az containerapp logs show -n cpp-test-container-app -g cpp-test-container-apps 

    See full output using: az containerapp show -n cpp-test-container-app -g cpp-test-container-apps 




    az container create --resource-group pp-test-container-apps --name cpp-test-app-aci --image ommazurecontainerregistry.azurecr.io/cpp-test-app-image --port 8080 --dns-name-label pg230-container-101 --location eastus