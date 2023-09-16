#Create group

    az group create --name aks-rg --location eastus


#Create an AKS cluster
    az aks create --name aks-cluster --resource-group aks-rg --enable-managed-identity --node-count 1 --enable-addons monitoring --generate-ssh-key
    SSH key files '/Users/pawgupta0/.ssh/id_rsa' and '/Users/pawgupta0/.ssh/id_rsa.pub' have been generated under ~/.ssh to allow SSH access to the VM. If using machines without permanent storage like Azure Cloud Shell without an attached file share, back up your keys to a safe location
{
  "aadProfile": null,
  "addonProfiles": {
    "omsagent": {
      "config": {
        "logAnalyticsWorkspaceResourceID": "/subscriptions/17e6b87f-6549-4a64-91e0-dbda9e0d5be2/resourceGroups/DefaultResourceGroup-EUS/providers/Microsoft.OperationalInsights/workspaces/DefaultWorkspace-17e6b87f-6549-4a64-91e0-dbda9e0d5be2-EUS",
        "useAADAuth": "true"
      },
      "enabled": true,
      "identity": null
    }
  },
  "agentPoolProfiles": [
    {
      "availabilityZones": null,
      "count": 1,
      "creationData": null,
      "currentOrchestratorVersion": "1.26.6",
      "enableAutoScaling": false,
      "enableEncryptionAtHost": false,
      "enableFips": false,
      "enableNodePublicIp": false,
      "enableUltraSsd": false,
      "gpuInstanceProfile": null,
      "hostGroupId": null,
      "kubeletConfig": null,
      "kubeletDiskType": "OS",
      "linuxOsConfig": null,
      "maxCount": null,
      "maxPods": 110,
      "minCount": null,
      "mode": "System",
      "name": "nodepool1",
      "nodeImageVersion": "AKSUbuntu-2204gen2containerd-202308.10.0",
      "nodeLabels": null,
      "nodePublicIpPrefixId": null,
      "nodeTaints": null,
      "orchestratorVersion": "1.26.6",
      "osDiskSizeGb": 128,
      "osDiskType": "Managed",
      "osSku": "Ubuntu",
      "osType": "Linux",
      "podSubnetId": null,
      "powerState": {
        "code": "Running"
      },
      "provisioningState": "Succeeded",
      "proximityPlacementGroupId": null,
      "scaleDownMode": null,
      "scaleSetEvictionPolicy": null,
      "scaleSetPriority": null,
      "spotMaxPrice": null,
      "tags": null,
      "type": "VirtualMachineScaleSets",
      "upgradeSettings": {
        "maxSurge": null
      },
      "vmSize": "Standard_DS2_v2",
      "vnetSubnetId": null,
      "workloadRuntime": null
    }
  ],
  "apiServerAccessProfile": null,
  "autoScalerProfile": null,
  "autoUpgradeProfile": null,
  "azureMonitorProfile": null,
  "azurePortalFqdn": "aks-cluste-aks-rg-17e6b8-ibbhmbmm.portal.hcp.eastus.azmk8s.io",
  "currentKubernetesVersion": "1.26.6",
  "disableLocalAccounts": false,
  "diskEncryptionSetId": null,
  "dnsPrefix": "aks-cluste-aks-rg-17e6b8",
  "enablePodSecurityPolicy": null,
  "enableRbac": true,
  "extendedLocation": null,
  "fqdn": "aks-cluste-aks-rg-17e6b8-ibbhmbmm.hcp.eastus.azmk8s.io",
  "fqdnSubdomain": null,
  "httpProxyConfig": null,
  "id": "/subscriptions/17e6b87f-6549-4a64-91e0-dbda9e0d5be2/resourcegroups/aks-rg/providers/Microsoft.ContainerService/managedClusters/aks-cluster",
  "identity": {
    "principalId": "f2d5efc6-2f53-4aea-b0b8-d5212006880f",
    "tenantId": "d52c9ea1-7c21-47b1-82a3-33a74b1f74b8",
    "type": "SystemAssigned",
    "userAssignedIdentities": null
  },
  "identityProfile": {
    "kubeletidentity": {
      "clientId": "a6f12ad0-3d5e-4301-a3f9-cd1c7c715fec",
      "objectId": "5888f04b-5556-4c8f-ae1d-a0f435165bcf",
      "resourceId": "/subscriptions/17e6b87f-6549-4a64-91e0-dbda9e0d5be2/resourcegroups/MC_aks-rg_aks-cluster_eastus/providers/Microsoft.ManagedIdentity/userAssignedIdentities/aks-cluster-agentpool"
    }
  },
  "kubernetesVersion": "1.26.6",
  "linuxProfile": {
    "adminUsername": "azureuser",
    "ssh": {
      "publicKeys": [
        {
          "keyData": "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDqYr1hq63/GPLg4JaXZwHtQ8fXuYVlljY/5OxruqL1i/+Jl0RxGgr6X3vlfKpP/xcmAVj+LWXLZOBStWfUO/61lXijnwjbb3wZp7jq4FgKcNMzhB2yOuIuc+GFjn35HiCHs4MtdD2GBh5bgHfo6jrVjomLYdv/Yq5/HoFNI7AXbX6lbmWXOPaxWXMaFGy5T47XsoPEg4M87sOcUQnz7hCJ3iIxVTh6tCcbg70DItwjysarozVrO0AkHtXVFv68XEyFLQLy4aG4ed2hQUTnrlzwCEcm9OyM9iSR54lH6btTt4KqPEh5fq/az7nmmOwKyy2zKpksXJbqLdOE2IYgRdRj"
        }
      ]
    }
  },
  "location": "eastus",
  "maxAgentPools": 100,
  "name": "aks-cluster",
  "networkProfile": {
    "dnsServiceIp": "10.0.0.10",
    "ipFamilies": [
      "IPv4"
    ],
    "loadBalancerProfile": {
      "allocatedOutboundPorts": null,
      "effectiveOutboundIPs": [
        {
          "id": "/subscriptions/17e6b87f-6549-4a64-91e0-dbda9e0d5be2/resourceGroups/MC_aks-rg_aks-cluster_eastus/providers/Microsoft.Network/publicIPAddresses/5ef34b31-08d9-4607-8ecf-474d8d91b235",
          "resourceGroup": "MC_aks-rg_aks-cluster_eastus"
        }
      ],
      "enableMultipleStandardLoadBalancers": null,
      "idleTimeoutInMinutes": null,
      "managedOutboundIPs": {
        "count": 1,
        "countIpv6": null
      },
      "outboundIPs": null,
      "outboundIpPrefixes": null
    },
    "loadBalancerSku": "Standard",
    "natGatewayProfile": null,
    "networkDataplane": null,
    "networkMode": null,
    "networkPlugin": "kubenet",
    "networkPluginMode": null,
    "networkPolicy": null,
    "outboundType": "loadBalancer",
    "podCidr": "10.244.0.0/16",
    "podCidrs": [
      "10.244.0.0/16"
    ],
    "serviceCidr": "10.0.0.0/16",
    "serviceCidrs": [
      "10.0.0.0/16"
    ]
  },
  "nodeResourceGroup": "MC_aks-rg_aks-cluster_eastus",
  "oidcIssuerProfile": {
    "enabled": false,
    "issuerUrl": null
  },
  "podIdentityProfile": null,
  "powerState": {
    "code": "Running"
  },
  "privateFqdn": null,
  "privateLinkResources": null,
  "provisioningState": "Succeeded",
  "publicNetworkAccess": null,
  "resourceGroup": "aks-rg",
  "securityProfile": {
    "azureKeyVaultKms": null,
    "defender": null,
    "imageCleaner": null,
    "workloadIdentity": null
  },
  "servicePrincipalProfile": {
    "clientId": "msi",
    "secret": null
  },
  "sku": {
    "name": "Base",
    "tier": "Free"
  },
  "storageProfile": {
    "blobCsiDriver": null,
    "diskCsiDriver": {
      "enabled": true
    },
    "fileCsiDriver": {
      "enabled": true
    },
    "snapshotController": {
      "enabled": true
    }
  },
  "supportPlan": "KubernetesOfficial",
  "systemData": null,
  "tags": null,
  "type": "Microsoft.ContainerService/ManagedClusters",
  "windowsProfile": null,
  "workloadAutoScalerProfile": {
    "keda": null
  }
}
bash-3.2$ ~


# Comamnds to see the resources created.

        bash-3.2$ az group list --out table
        Name                          Location    Status
        ----------------------------  ----------  ---------
        NetworkWatcherRG              eastus      Succeeded
        DefaultResourceGroup-EUS      eastus      Succeeded
        aks-rg                        eastus      Succeeded
        MC_aks-rg_aks-cluster_eastus  eastus      Succeeded


        bash-3.2$ az resource list  -o table
        Name                                                       ResourceGroup                 Location    Type                                              Status
        ---------------------------------------------------------  ----------------------------  ----------  ------------------------------------------------  --------
        aks-cluster                                                aks-rg                        eastus      Microsoft.ContainerService/managedClusters
        MSCI-eastus-aks-cluster                                    aks-rg                        eastus      Microsoft.Insights/dataCollectionRules
        DefaultWorkspace-17e6b87f-6549-4a64-91e0-dbda9e0d5be2-EUS  DefaultResourceGroup-EUS      eastus      Microsoft.OperationalInsights/workspaces
        aks-nodepool1-36323758-vmss                                MC_aks-rg_aks-cluster_eastus  eastus      Microsoft.Compute/virtualMachineScaleSets
        aks-cluster-agentpool                                      MC_aks-rg_aks-cluster_eastus  eastus      Microsoft.ManagedIdentity/userAssignedIdentities
        kubernetes                                                 MC_aks-rg_aks-cluster_eastus  eastus      Microsoft.Network/loadBalancers
        aks-agentpool-36393166-nsg                                 MC_aks-rg_aks-cluster_eastus  eastus      Microsoft.Network/networkSecurityGroups
        5ef34b31-08d9-4607-8ecf-474d8d91b235                       MC_aks-rg_aks-cluster_eastus  eastus      Microsoft.Network/publicIPAddresses
        aks-agentpool-36393166-routetable                          MC_aks-rg_aks-cluster_eastus  eastus      Microsoft.Network/routeTables
        aks-vnet-36393166                                          MC_aks-rg_aks-cluster_eastus  eastus      Microsoft.Network/virtualNetworks
        NetworkWatcher_eastus                                      NetworkWatcherRG              eastus      Microsoft.Network/networkWatchers


        bash-3.2$ az resource list  -g aks-rg -o table
        Name                     ResourceGroup    Location    Type                                        Status
        -----------------------  ---------------  ----------  ------------------------------------------  --------
        aks-cluster              aks-rg           eastus      Microsoft.ContainerService/managedClusters
        MSCI-eastus-aks-cluster  aks-rg           eastus      Microsoft.Insights/dataCollectionRules



        bash-3.2$ az resource list  -g MC_aks-rg_aks-cluster_eastus  -o table
        Name                                  ResourceGroup                 Location    Type                                              Status
        ------------------------------------  ----------------------------  ----------  ------------------------------------------------  --------
        aks-nodepool1-36323758-vmss           MC_aks-rg_aks-cluster_eastus  eastus      Microsoft.Compute/virtualMachineScaleSets
        aks-cluster-agentpool                 MC_aks-rg_aks-cluster_eastus  eastus      Microsoft.ManagedIdentity/userAssignedIdentities
        kubernetes                            MC_aks-rg_aks-cluster_eastus  eastus      Microsoft.Network/loadBalancers
        aks-agentpool-36393166-nsg            MC_aks-rg_aks-cluster_eastus  eastus      Microsoft.Network/networkSecurityGroups
        5ef34b31-08d9-4607-8ecf-474d8d91b235  MC_aks-rg_aks-cluster_eastus  eastus      Microsoft.Network/publicIPAddresses
        aks-agentpool-36393166-routetable     MC_aks-rg_aks-cluster_eastus  eastus      Microsoft.Network/routeTables
        aks-vnet-36393166                     MC_aks-rg_aks-cluster_eastus  eastus      Microsoft.Network/virtualNetworks

#Connect to the cluster

    #Install kubectl locally using the az aks install-cli command.
    az aks install-cli

    #Configure kubectl to connect to your Kubernetes cluster using the az aks get-credentials command.
    az aks get-credentials --resource-group aks-rg --name aks-cluster
    Merged "aks-cluster" as current context in /Users/pawgupta0/.kube/config


    #Verify the connection to your cluster using the kubectl get command. This command returns a list of the cluster nodes.
        kubectl get nodes
        NAME                                STATUS   ROLES   AGE   VERSION
        aks-nodepool1-36323758-vmss000000   Ready    agent   19m   v1.26.6



# Deploy the application

    # Create a file named azure-vote.yaml and copy in the following manifest.
            apiVersion: apps/v1
            kind: Deployment
            metadata:
            name: azure-vote-back
            spec:
            replicas: 1
            selector:
                matchLabels:
                app: azure-vote-back
            template:
                metadata:
                labels:
                    app: azure-vote-back
                spec:
                nodeSelector:
                    "kubernetes.io/os": linux
                containers:
                - name: azure-vote-back
                    image: mcr.microsoft.com/oss/bitnami/redis:6.0.8
                    env:
                    - name: ALLOW_EMPTY_PASSWORD
                    value: "yes"
                    resources:
                    requests:
                        cpu: 100m
                        memory: 128Mi
                    limits:
                        cpu: 250m
                        memory: 256Mi
                    ports:
                    - containerPort: 6379
                    name: redis
            ---
            apiVersion: v1
            kind: Service
            metadata:
            name: azure-vote-back
            spec:
            ports:
            - port: 6379
            selector:
                app: azure-vote-back
            ---
            apiVersion: apps/v1
            kind: Deployment
            metadata:
            name: azure-vote-front
            spec:
            replicas: 1
            selector:
                matchLabels:
                app: azure-vote-front
            template:
                metadata:
                labels:
                    app: azure-vote-front
                spec:
                nodeSelector:
                    "kubernetes.io/os": linux
                containers:
                - name: azure-vote-front
                    image: mcr.microsoft.com/azuredocs/azure-vote-front:v1
                    resources:
                    requests:
                        cpu: 100m
                        memory: 128Mi
                    limits:
                        cpu: 250m
                        memory: 256Mi
                    ports:
                    - containerPort: 80
                    env:
                    - name: REDIS
                    value: "azure-vote-back"
            ---
            apiVersion: v1
            kind: Service
            metadata:
            name: azure-vote-front
            spec:
            type: LoadBalancer
            ports:
            - port: 80
            selector:
                app: azure-vote-front


    # Deploy the application using the kubectl apply command and specify the name of your YAML manifest.
        cd /Users/pawgupta0/Pawanesh/development/AzureCloud/AzureKubernetesService
        kubectl apply -f azure-vote.yaml


            kubectl apply -f azure-vote.yaml 
            deployment.apps/azure-vote-back created
            service/azure-vote-back created
            deployment.apps/azure-vote-front created
            service/azure-vote-front created


    #Test the application

    #Monitor progress using the kubectl get service command with the --watch argument.

                kubectl get service azure-vote-front --watch

                kubectl get service azure-vote-front --watch
                NAME               TYPE           CLUSTER-IP     EXTERNAL-IP      PORT(S)        AGE
                azure-vote-front   LoadBalancer   10.0.155.224   20.241.218.220   80:30264/TCP   18m


    #Debug the container node.
        #Get nodes
        kubectl get nodes -o wide


        kubectl get nodes -o wide
        NAME                                STATUS   ROLES   AGE     VERSION   INTERNAL-IP   EXTERNAL-IP   OS-IMAGE             KERNEL-VERSION      CONTAINER-RUNTIME
        aks-nodepool1-36323758-vmss000000   Ready    agent   3h15m   v1.26.6   10.224.0.4    <none>        Ubuntu 22.04.3 LTS   5.15.0-1042-azure   containerd://1.7.1+azure-1


        #Use the kubectl debug command to run a container image on the node to connect to it. The following command starts a privileged container on your node and connects to it.

        kubectl debug node/aks-nodepool1-36323758-vmss000000 -it --image=mcr.microsoft.com/dotnet/runtime-deps:6.0
        
        Creating debugging pod node-debugger-aks-nodepool1-36323758-vmss000000-t5cm5 with container debugger on node aks-nodepool1-36323758-vmss000000.
        If you don't see a command prompt, try pressing enter.

        #After debugging delete the debug pod.
        kubectl delete pod node-debugger-aks-nodepool1-36323758-vmss000000-t5cm5
        pod "node-debugger-aks-nodepool1-36323758-vmss000000-t5cm5" deleted



        kubectl get pods -o wide
        NAME                               READY   STATUS    RESTARTS   AGE   IP            NODE                                NOMINATED NODE   READINESS GATES
        azure-vote-back-65c595548d-b56vt   1/1     Running   0          79m   10.244.0.15   aks-nodepool1-36323758-vmss000000   <none>           <none>
        azure-vote-front-d99b7676c-dkz7d   1/1     Running   0          79m   10.244.0.16   aks-nodepool1-36323758-vmss000000   <none>           <none>

        kubectl get deployment
        NAME               READY   UP-TO-DATE   AVAILABLE   AGE
        azure-vote-back    1/1     1            1           80m
        azure-vote-front   1/1     1            1           80m

        kubectl get deployment -o wide
        NAME               READY   UP-TO-DATE   AVAILABLE   AGE   CONTAINERS         IMAGES                                            SELECTOR
        azure-vote-back    1/1     1            1           80m   azure-vote-back    mcr.microsoft.com/oss/bitnami/redis:6.0.8         app=azure-vote-back
        azure-vote-front   1/1     1            1           80m   azure-vote-front   mcr.microsoft.com/azuredocs/azure-vote-front:v1   app=azure-vote-front

        #Get into ruuning pod container
        kubectl exec --stdin --tty azure-vote-back-65c595548d-b56vt -- /bin/bash
        I have no name!@azure-vote-back-65c595548d-b56vt:/$ 
        I have no name!@azure-vote-back-65c595548d-b56vt:/$ ls -ltr
        total 76
        drwxr-xr-x   1 root root 4096 Sep 25  2017 lib
        drwxr-xr-x   1 root root 4096 Jul 21  2020 var
        drwxr-xr-x   2 root root 4096 Jul 21  2020 srv
        drwx------   2 root root 4096 Jul 21  2020 root
        drwxr-xr-x   2 root root 4096 Jul 21  2020 mnt
        drwxr-xr-x   2 root root 4096 Jul 21  2020 media
        drwxr-xr-x   2 root root 4096 Jul 21  2020 lib64
        drwxr-xr-x   2 root root 4096 Jul 21  2020 home
        drwxr-xr-x   2 root root 4096 Jul 21  2020 boot
        drwxr-xr-x   1 root root 4096 Sep 28  2020 usr
        drwxr-xr-x   1 root root 4096 Sep 28  2020 opt
        drwxr-xr-x   1 root root 4096 Sep 28  2020 sbin
        drwxr-xr-x   1 root root 4096 Sep 28  2020 bin
        lrwxrwxrwx   1 root root   40 Sep 28  2020 entrypoint.sh -> /opt/bitnami/scripts/redis/entrypoint.sh
        lrwxrwxrwx   1 root root   33 Sep 28  2020 run.sh -> /opt/bitnami/scripts/redis/run.sh
        drwxrwxr-x   1 root root 4096 Sep 28  2020 bitnami
        dr-xr-xr-x  12 root root    0 Aug 26 19:29 sys
        drwxr-xr-x   1 root root 4096 Aug 26 19:29 run
        dr-xr-xr-x 276 root root    0 Aug 26 19:29 proc
        drwxr-xr-x   1 root root 4096 Aug 26 19:29 etc
        drwxr-xr-x   5 root root  360 Aug 26 19:29 dev
        drwxrwxrwt   1 root root 4096 Aug 26 19:29 tmp

        I have no name!@azure-vote-back-65c595548d-b56vt:/$ hostname
        azure-vote-back-65c595548d-b56vt


        kubectl logs azure-vote-back-65c595548d-b56vt
        redis 19:29:16.43 
        redis 19:29:16.44 Welcome to the Bitnami redis container
        redis 19:29:16.44 Subscribe to project updates by watching https://github.com/bitnami/bitnami-docker-redis
        redis 19:29:16.44 Submit issues and feature requests at https://github.com/bitnami/bitnami-docker-redis/issues
        redis 19:29:16.44 
        redis 19:29:16.44 INFO  ==> ** Starting Redis setup **
        redis 19:29:16.53 WARN  ==> You set the environment variable ALLOW_EMPTY_PASSWORD=yes. For safety reasons, do not use this flag in a production environment.
        redis 19:29:16.54 INFO  ==> Initializing Redis
        redis 19:29:16.55 INFO  ==> Setting Redis config file
        redis 19:29:16.65 INFO  ==> ** Redis setup finished! **

        redis 19:29:16.74 INFO  ==> ** Starting Redis **
        1:C 26 Aug 2023 19:29:16.753 # oO0OoO0OoO0Oo Redis is starting oO0OoO0OoO0Oo
        1:C 26 Aug 2023 19:29:16.753 # Redis version=6.0.8, bits=64, commit=00000000, modified=0, pid=1, just started
        1:C 26 Aug 2023 19:29:16.753 # Configuration loaded
                        _._                                                  
                _.-``__ ''-._                                             
            _.-``    `.  `_.  ''-._           Redis 6.0.8 (00000000/0) 64 bit
        .-`` .-```.  ```\/    _.,_ ''-._                                   
        (    '      ,       .-`  | `,    )     Running in standalone mode
        |`-._`-...-` __...-.``-._|'` _.-'|     Port: 6379
        |    `-._   `._    /     _.-'    |     PID: 1
        `-._    `-._  `-./  _.-'    _.-'                                   
        |`-._`-._    `-.__.-'    _.-'_.-'|                                  
        |    `-._`-._        _.-'_.-'    |           http://redis.io        
        `-._    `-._`-.__.-'_.-'    _.-'                                   
        |`-._`-._    `-.__.-'    _.-'_.-'|                                  
        |    `-._`-._        _.-'_.-'    |                                  
        `-._    `-._`-.__.-'_.-'    _.-'                                   
            `-._    `-.__.-'    _.-'                                       
                `-._        _.-'                                           
                    `-.__.-'                                               

        1:M 26 Aug 2023 19:29:16.755 # Server initialized
        1:M 26 Aug 2023 19:29:16.755 # WARNING you have Transparent Huge Pages (THP) support enabled in your kernel. This will create latency and memory usage issues with Redis. To fix this issue run the command 'echo madvise > /sys/kernel/mm/transparent_hugepage/enabled' as root, and add it to your /etc/rc.local in order to retain the setting after a reboot. Redis must be restarted after THP is disabled (set to 'madvise' or 'never').
        1:M 26 Aug 2023 19:29:16.756 * Ready to accept connections
        1:M 26 Aug 2023 19:44:17.015 * 1 changes in 900 seconds. Saving...
        1:M 26 Aug 2023 19:44:17.015 * Background saving started by pid 39
        39:C 26 Aug 2023 19:44:17.025 * DB saved on disk
        39:C 26 Aug 2023 19:44:17.026 * RDB: 0 MB of memory used by copy-on-write
        1:M 26 Aug 2023 19:44:17.116 * Background saving terminated with success
        1:M 26 Aug 2023 19:59:18.061 * 1 changes in 900 seconds. Saving...
        1:M 26 Aug 2023 19:59:18.062 * Background saving started by pid 40
        40:C 26 Aug 2023 19:59:18.070 * DB saved on disk
        40:C 26 Aug 2023 19:59:18.071 * RDB: 0 MB of memory used by copy-on-write
        1:M 26 Aug 2023 19:59:18.162 * Background saving terminated with success


    kubectl exec azure-vote-back-65c595548d-b56vt  -- date
    Sat Aug 26 20:57:58 UTC 2023


    #Cleanup

    az group delete --name aks-rg
    Are you sure you want to perform this operation? (y/n): y
    | Running ..
