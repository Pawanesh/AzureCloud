#List resource groups

az group list --output table

        (base) pawgupta0@WKMZT1D2F51B AzureCloud % az group list --output table
        Name                      Location    Status
        ------------------------  ----------  ---------
        test-resource-group       eastus      Succeeded
        NetworkWatcherRG          eastus      Succeeded
        DefaultResourceGroup-EUS  eastus      Succeeded


#Create resource group for container

az group create --name acr-rg --location eastus

        (base) pawgupta0@WKMZT1D2F51B AzureCloud % az group create --name acr-rg --location eastus
        {
        "id": "/subscriptions/17e6b87f-6549-4a64-91e0-dbda9e0d5be2/resourceGroups/acr-rg",
        "location": "eastus",
        "managedBy": null,
        "name": "acr-rg",
        "properties": {
            "provisioningState": "Succeeded"
        },
        "tags": null,
        "type": "Microsoft.Resources/resourceGroups"
        }


#Create container registry
az acr create --resource-group acr-rg --name pawaneshcontainerregistry --sku Basic

    (base) pawgupta0@WKMZT1D2F51B AzureCloud % az acr create --resource-group acr-rg --name pawaneshcontainerregistry --sku Basic
    {
    "adminUserEnabled": false,
    "anonymousPullEnabled": false,
    "creationDate": "2023-08-18T17:39:37.591733+00:00",
    "dataEndpointEnabled": false,
    "dataEndpointHostNames": [],
    "encryption": {
        "keyVaultProperties": null,
        "status": "disabled"
    },
    "id": "/subscriptions/17e6b87f-6549-4a64-91e0-dbda9e0d5be2/resourceGroups/acr-rg/providers/Microsoft.ContainerRegistry/registries/pawaneshcontainerregistry",
    "identity": null,
    "location": "eastus",
    "loginServer": "pawaneshcontainerregistry.azurecr.io",
    "name": "pawaneshcontainerregistry",
    "networkRuleBypassOptions": "AzureServices",
    "networkRuleSet": null,
    "policies": {
        "azureAdAuthenticationAsArmPolicy": {
        "status": "enabled"
        },
        "exportPolicy": {
        "status": "enabled"
        },
        "quarantinePolicy": {
        "status": "disabled"
        },
        "retentionPolicy": {
        "days": 7,
        "lastUpdatedTime": "2023-08-18T17:39:43.974907+00:00",
        "status": "disabled"
        },
        "softDeletePolicy": {
        "lastUpdatedTime": "2023-08-18T17:39:43.974956+00:00",
        "retentionDays": 7,
        "status": "disabled"
        },
        "trustPolicy": {
        "status": "disabled",
        "type": "Notary"
        }
    },
    "privateEndpointConnections": [],
    "provisioningState": "Succeeded",
    "publicNetworkAccess": "Enabled",
    "resourceGroup": "acr-rg",
    "sku": {
        "name": "Basic",
        "tier": "Basic"
    },
    "status": null,
    "systemData": {
        "createdAt": "2023-08-18T17:39:37.591733+00:00",
        "createdBy": "pawgupta0@publicisgroupe.net",
        "createdByType": "User",
        "lastModifiedAt": "2023-08-18T17:39:37.591733+00:00",
        "lastModifiedBy": "pawgupta0@publicisgroupe.net",
        "lastModifiedByType": "User"
    },
    "tags": {},
    "type": "Microsoft.ContainerRegistry/registries",
    "zoneRedundancy": "Disabled"
    }


# List container registry
    az acr list --output table

    (base) pawgupta0@WKMZT1D2F51B AzureCloud % az acr list --output table
    NAME                       RESOURCE GROUP    LOCATION    SKU    LOGIN SERVER                          CREATION DATE         ADMIN ENABLED
    -------------------------  ----------------  ----------  -----  ------------------------------------  --------------------  ---------------
    pawaneshcontainerregistry  acr-rg            eastus      Basic  pawaneshcontainerregistry.azurecr.io  2023-08-18T17:39:37Z  False

#list the Resources

az resource list --output table

        (base) pawgupta0@WKMZT1D2F51B HelloWorld % az resource list --output table
        Name                       ResourceGroup    Location    Type                                    Status
        -------------------------  ---------------  ----------  --------------------------------------  --------
        pawaneshcontainerregistry  acr-rg           eastus      Microsoft.ContainerRegistry/registries


#### Build and push image from a Dockerfile

# Create container registry
    az acr build --image sample/helloworld:v1  --registry pawaneshcontainerregistry --file Dockerfile .

# Create image and push to registry pawaneshcontainerregistry
az acr build --image sample/helloworld:v1  --registry pawaneshcontainerregistry --file Dockerfile .

        pwd
        /Users/pawgupta0/Pawanesh/development/AzureCloud/Container/HelloWorld

        (base) pawgupta0@WKMZT1D2F51B HelloWorld % az acr build --image sample/helloworld:v1  --registry pawaneshcontainerregistry --file Dockerfile .

        - image:
            registry: pawaneshcontainerregistry.azurecr.io
            repository: sample/helloworld
            tag: v1
            digest: sha256:92c7f9c92844bbbb5d0a101b22f7c2a7949e40f8ea90c8b3bc396879d95e899a
        runtime-dependency:
            registry: mcr.microsoft.com
            repository: hello-world
            tag: latest
            digest: sha256:92c7f9c92844bbbb5d0a101b22f7c2a7949e40f8ea90c8b3bc396879d95e899a
        git: {}


Run ID: ca4 was successful after 8s


# List the images from container registry pawaneshcontainerregistry
az acr repository list --name pawaneshcontainerregistry --output table                             

        (base) pawgupta0@WKMZT1D2F51B HelloWorld % az acr repository list --name pawaneshcontainerregistry --output table                             
        Result
        -----------------
        sample/helloworld

# List the tags of image

        (base) pawgupta0@WKMZT1D2F51B HelloWorld % az acr repository show-tags --name pawaneshcontainerregistry --repository sample/helloworld --output table
        Result
        --------
        v1


#### Run the image in acr
az acr run --registry pawaneshcontainerregistry --cmd 'pawaneshcontainerregistry.azurecr.io/sample/helloworld:v1' /dev/null

        (base) pawgupta0@WKMZT1D2F51B HelloWorld % az acr run --registry pawaneshcontainerregistry --cmd 'pawaneshcontainerregistry.azurecr.io/sample/helloworld:v1' /dev/null
        Queued a run with ID: ca6
        Waiting for an agent...
        2023/08/18 19:45:57 Alias support enabled for version >= 1.1.0, please see https://aka.ms/acr/tasks/task-aliases for more information.
        2023/08/18 19:45:57 Creating Docker network: acb_default_network, driver: 'bridge'
        2023/08/18 19:45:58 Successfully set up Docker network: acb_default_network
        2023/08/18 19:45:58 Setting up Docker configuration...
        2023/08/18 19:45:58 Successfully set up Docker configuration
        2023/08/18 19:45:58 Logging in to registry: pawaneshcontainerregistry.azurecr.io
        2023/08/18 19:45:59 Successfully logged into pawaneshcontainerregistry.azurecr.io
        2023/08/18 19:45:59 Executing step ID: acb_step_0. Timeout(sec): 600, Working directory: '', Network: 'acb_default_network'
        2023/08/18 19:45:59 Launching container with name: acb_step_0
        Unable to find image 'pawaneshcontainerregistry.azurecr.io/sample/helloworld:v1' locally
        v1: Pulling from sample/helloworld
        1b930d010525: Pulling fs layer
        1b930d010525: Verifying Checksum
        1b930d010525: Download complete
        1b930d010525: Pull complete
        Digest: sha256:92c7f9c92844bbbb5d0a101b22f7c2a7949e40f8ea90c8b3bc396879d95e899a
        Status: Downloaded newer image for pawaneshcontainerregistry.azurecr.io/sample/helloworld:v1

        Hello from Docker!
        This message shows that your installation appears to be working correctly.

        To generate this message, Docker took the following steps:
        1. The Docker client contacted the Docker daemon.
        2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
            (amd64)
        3. The Docker daemon created a new container from that image which runs the
            executable that produces the output you are currently reading.
        4. The Docker daemon streamed that output to the Docker client, which sent it
            to your terminal.

        To try something more ambitious, you can run an Ubuntu container with:
        $ docker run -it ubuntu bash

        Share images, automate workflows, and more with a free Docker ID:
        https://hub.docker.com/

        For more examples and ideas, visit:
        https://docs.docker.com/get-started/

        2023/08/18 19:45:59 Successfully executed container: acb_step_0
        2023/08/18 19:45:59 Step ID: acb_step_0 marked as successful (elapsed time in seconds: 0.754947)

        Run ID: ca6 was successful after 3s


# Another way to run the container image in acr.
az acr run --registry pawaneshcontainerregistry --cmd 'docker run pawaneshcontainerregistry.azurecr.io/sample/helloworld:v1' /dev/null

            (base) pawgupta0@WKMZT1D2F51B HelloWorld % az acr run --registry pawaneshcontainerregistry --cmd 'docker run pawaneshcontainerregistry.azurecr.io/sample/helloworld:v1' /dev/null
            Queued a run with ID: cax
            Waiting for an agent...
            2023/08/18 20:36:19 Alias support enabled for version >= 1.1.0, please see https://aka.ms/acr/tasks/task-aliases for more information.
            2023/08/18 20:36:19 Creating Docker network: acb_default_network, driver: 'bridge'
            2023/08/18 20:36:19 Successfully set up Docker network: acb_default_network
            2023/08/18 20:36:19 Setting up Docker configuration...
            2023/08/18 20:36:20 Successfully set up Docker configuration
            2023/08/18 20:36:20 Logging in to registry: pawaneshcontainerregistry.azurecr.io
            2023/08/18 20:36:21 Successfully logged into pawaneshcontainerregistry.azurecr.io
            2023/08/18 20:36:21 Executing step ID: acb_step_0. Timeout(sec): 600, Working directory: '', Network: 'acb_default_network'
            2023/08/18 20:36:21 Launching container with name: acb_step_0
            Unable to find image 'pawaneshcontainerregistry.azurecr.io/sample/helloworld:v1' locally
            v1: Pulling from sample/helloworld
            1b930d010525: Pulling fs layer
            1b930d010525: Verifying Checksum
            1b930d010525: Download complete
            1b930d010525: Pull complete
            Digest: sha256:92c7f9c92844bbbb5d0a101b22f7c2a7949e40f8ea90c8b3bc396879d95e899a
            Status: Downloaded newer image for pawaneshcontainerregistry.azurecr.io/sample/helloworld:v1

            Hello from Docker!
            This message shows that your installation appears to be working correctly.

            To generate this message, Docker took the following steps:
            1. The Docker client contacted the Docker daemon.
            2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
                (amd64)
            3. The Docker daemon created a new container from that image which runs the
                executable that produces the output you are currently reading.
            4. The Docker daemon streamed that output to the Docker client, which sent it
                to your terminal.

            To try something more ambitious, you can run an Ubuntu container with:
            $ docker run -it ubuntu bash

            Share images, automate workflows, and more with a free Docker ID:
            https://hub.docker.com/

            For more examples and ideas, visit:
            https://docs.docker.com/get-started/

            2023/08/18 20:36:22 Successfully executed container: acb_step_0
            2023/08/18 20:36:22 Step ID: acb_step_0 marked as successful (elapsed time in seconds: 1.694140)

            Run ID: cax was successful after 5s


# Running container using ACI (azure container instance)

az container create --resource-group acr-rg --name helloworldcontainer --image pawaneshcontainerregistry.azurecr.io/sample/helloworld:v1 --location eastus --output table

            (base) pawgupta0@WKMZT1D2F51B HelloWorld % az container create --resource-group acr-rg --name helloworldcontainer --image pawaneshcontainerregistry.azurecr.io/sample/helloworld:v1 --location eastus --output table
            Image registry username: pawaneshcontainerregistry 
            Image registry password: 
            Name                 ResourceGroup    Status    Image                                                      CPU/Memory       OsType    Location
            -------------------  ---------------  --------  ---------------------------------------------------------  ---------------  --------  ----------
            helloworldcontainer  acr-rg           Running   pawaneshcontainerregistry.azurecr.io/sample/helloworld:v1  1.0 core/1.5 gb  Linux     eastus


############# Azure web app container ########
pwd: /Users/pawgupta0/Pawanesh/development/AzureCloud/AzureContainerRegistry/WebApp
#Build image
    docker build  . -t webappimage:v1 -f ./DockerFile

#Run image
    docker run --rm -it -p 4000:80  --name webapp-container webappimage:v1

#Debug comtainer
    docker run --rm --entrypoint /bin/bash -it -p 3000:3000  --name webapp-container webappimage:v1


#Create resource group
    az group create --name acr-rg --location eastus


#Create acr 
    az acr create --name acrpg230 -g acr-rg --sku Standard  


#Enabled admin access to acr

#Login into acr using docker
    docker login acrpg230.azurecr.io 


#Docker push to push image into acr
    docker tag webappimage:v1 acrpg230.azurecr.io/webappimage:v1
    docker push acrpg230.azurecr.io/webappimage:v1

#Create web app using image from acr and test
    https://pg230app.azurewebsites.net/


#Display acr
    az acr  show --name acrpg230 -o table
    NAME      RESOURCE GROUP    LOCATION    SKU       LOGIN SERVER         CREATION DATE         ADMIN ENABLED
    --------  ----------------  ----------  --------  -------------------  --------------------  ---------------
    acrpg230  acr-rg            eastus      Standard  acrpg230.azurecr.io  2023-10-10T13:26:34Z  True


#Display repositries in acr
    az acr repository list --name acrpg230 -o table
    Result
    --------------
    sample/webpapp
    webappimage


#Create a container in a container group using container image from Azure Container Registry.
        az container create -g acr-rg --name containerwebapp --image acrpg230.azurecr.io/webappimage:v1 --registry-password 70iq87Usb91wCoF8Fi9GtsoWX9tMJsCQipGlzRdc9b+ACRBYchUO --ports 80 443
