#Connect linux vm
ssh -i sshkeys/test-vm-2_key.pem azureuser@40.71.26.76 

ssh -i sshkeys/vm-test-key.pem azureuser@104.45.148.195


#Connect linux vm via cloud shell
az ssh vm --resource-group vm-rg --vm-name vm-test --subscription 17e6b87f-6549-4a64-91e0-dbda9e0d5be2

#Install homebrew
/bin/bash -c "$(curl --insecure -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

#Install azure cli
brew update && brew install azure-cli

#Azure login
az login
A web browser has been opened at https://login.microsoftonline.com/organizations/oauth2/v2.0/authorize. Please continue the login in the web browser. If no web browser is available or if the web browser fails to open, use device code flow with `az login --use-device-code`.
The following tenants don't contain accessible subscriptions. Use 'az login --allow-no-subscriptions' to have tenant level access.
32584af0-4c9f-4776-a3e4-a03cf2d03b9f 'BDO O365 GP PRD APAC'
[
  {
    "cloudName": "AzureCloud",
    "homeTenantId": "d52c9ea1-7c21-47b1-82a3-33a74b1f74b8",
    "id": "17e6b87f-6549-4a64-91e0-dbda9e0d5be2",
    "isDefault": true,
    "managedByTenants": [],
    "name": "pawgupta0@publicisgroupe.net",
    "state": "Enabled",
    "tenantId": "d52c9ea1-7c21-47b1-82a3-33a74b1f74b8",
    "user": {
      "name": "pawgupta0@publicisgroupe.net",
      "type": "user"
    }
  }
]




https://durablefuncpg230.azurewebsites.net/api/orchestrators/Orch1?code=rwgqzodiambSjytre4SHeRML3jmDSLqEvA9cxUJ1WCoAAzFu7kUaWA==


https://durablefuncpg230.azurewebsites.net/api/orchestrators/{functionName}?code=rwgqzodiambSjytre4SHeRML3jmDSLqEvA9cxUJ1WCoAAzFu7kUaWA==





https://storageaccpg230.blob.core.windows.net/?sv=2022-11-02&ss=b&srt=c&sp=rtf&se=2023-10-25T21:21:36Z&st=2023-10-25T13:21:36Z&spr=https&sig=NF%2B0zNIG0aTm2T9RJMtTuoR04yTkpdDhc3aYqvuZQuQ%3D

https://storageaccpg230.blob.core.windows.net/container1?sp=rl&st=2023-10-25T13:30:33Z&se=2023-10-25T21:30:33Z&spr=https&sv=2022-11-02&sr=c&sig=d1mPuUMWTuoDEzx1OiXNnaWOBvuJcrzIgkqRm6zlaUU%3D

AccountEndpoint=https://cosmos-pg230.documents.azure.com:443/;AccountKey=gS9CG3MzniT4wiOElq4FHuZdIBPlZJ6hkuS5BRmkng5pmh1uW62h91ptwSPxmrwL9I7GvuALI90LACDbLAs9zw==;

AccountEndpoint=https://cosmos-pg230.documents.azure.com:443/;AccountKey=gS9CG3MzniT4wiOElq4FHuZdIBPlZJ6hkuS5BRmkng5pmh1uW62h91ptwSPxmrwL9I7GvuALI90LACDbLAs9zw==;