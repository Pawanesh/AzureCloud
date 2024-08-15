terraform {
  required_providers {
    azurerm = {
      source = "hashicorp/azurerm"
      version = "3.115.0"
    }
    azapi = {
      source  = "Azure/azapi"
      version = "~> 1.8.0"
    }
  }
}



provider "azurerm" {
  subscription_id = "17e6b87f-6549-4a64-91e0-dbda9e0d5be2"
  tenant_id = "d52c9ea1-7c21-47b1-82a3-33a74b1f74b8"
  features {}
}

resource "azurerm_resource_group" "omm_dev_monitor_resource_group" {
  name = "omm-dev-monitor-resource-group"
  location = "East US"

  tags = {
    environment = "OMDEV"
  }
}

resource "azurerm_storage_account" "omm_dev_monitor_storage_account" {
  name                     = "ommdevstorageacc001"
  resource_group_name      = azurerm_resource_group.omm_dev_monitor_resource_group.name
  location                 = azurerm_resource_group.omm_dev_monitor_resource_group.location
  account_tier             = "Standard"
  account_replication_type = "LRS"

  tags = {
    environment = "OMDEV"
  }
}


resource "azurerm_virtual_network" "omm_dev_network" {
  name                = "omm-dev-network"
  address_space       = ["10.0.0.0/16"]
  location            = azurerm_resource_group.omm_dev_monitor_resource_group.location
  resource_group_name = azurerm_resource_group.omm_dev_monitor_resource_group.name
}

resource "azurerm_subnet" "omm_dev_subnetwork" {
  name                 = "internal"
  resource_group_name  = azurerm_resource_group.omm_dev_monitor_resource_group.name
  virtual_network_name = azurerm_virtual_network.omm_dev_network.name
  address_prefixes     = ["10.0.2.0/24"]
}

resource "azurerm_public_ip" "gis_pip_vm_01" {
  name                = "gis-pip-vm-01"
  resource_group_name = azurerm_resource_group.omm_dev_monitor_resource_group.name
  location            = azurerm_resource_group.omm_dev_monitor_resource_group.location
  allocation_method   = "Static"

  tags = {
    environment = "OMDEV"
  }
}

resource "azurerm_network_interface" "omm_dev_network_interface" {
  name                = "omm-dev-nic"
  location            = azurerm_resource_group.omm_dev_monitor_resource_group.location
  resource_group_name = azurerm_resource_group.omm_dev_monitor_resource_group.name

  ip_configuration {
    name                          = "external"
    subnet_id                     = azurerm_subnet.omm_dev_subnetwork.id
    private_ip_address_allocation = "Dynamic"
    public_ip_address_id = azurerm_public_ip.gis_pip_vm_01.id
  }
}



resource "azurerm_linux_virtual_machine" "gis_vm_01" {
  name                = "gis-vm-01"
  resource_group_name = azurerm_resource_group.omm_dev_monitor_resource_group.name
  location            = azurerm_resource_group.omm_dev_monitor_resource_group.location
  size                = "Standard_B1s"
  admin_username      = "azureuser"

  network_interface_ids = [
    azurerm_network_interface.omm_dev_network_interface.id,
  ]

  admin_ssh_key {
    username   = "azureuser"
    public_key = file("~/.ssh/id_rsa.pub")
  }

  os_disk {
    caching              = "ReadWrite"
    storage_account_type = "Standard_LRS"
  }

  source_image_reference {
    publisher = "RedHat"
    offer     = "RHEL"
    sku       = "87-gen2"
    version   = "latest"
  }
  
}



resource "azurerm_public_ip" "grds_pip_vm_01" {
  name                = "grds-pip-vm-01"
  resource_group_name = azurerm_resource_group.omm_dev_monitor_resource_group.name
  location            = azurerm_resource_group.omm_dev_monitor_resource_group.location
  allocation_method   = "Static"

  tags = {
    environment = "OMDEV"
  }
}

resource "azurerm_network_interface" "omm_dev_grds_vm_01_network_interface" {
  name                = "omm-dev-grds-01-nic"
  location            = azurerm_resource_group.omm_dev_monitor_resource_group.location
  resource_group_name = azurerm_resource_group.omm_dev_monitor_resource_group.name

  ip_configuration {
    name                          = "external"
    subnet_id                     = azurerm_subnet.omm_dev_subnetwork.id
    private_ip_address_allocation = "Dynamic"
    public_ip_address_id = azurerm_public_ip.grds_pip_vm_01.id
  }
}



resource "azurerm_linux_virtual_machine" "grds_vm_01" {
  name                = "grds-vm-01"
  resource_group_name = azurerm_resource_group.omm_dev_monitor_resource_group.name
  location            = azurerm_resource_group.omm_dev_monitor_resource_group.location
  size                = "Standard_B1s"
  admin_username      = "azureuser"

  network_interface_ids = [
    azurerm_network_interface.omm_dev_grds_vm_01_network_interface.id,
  ]

  admin_ssh_key {
    username   = "azureuser"
    public_key = file("~/.ssh/id_rsa.pub")
  }

  os_disk {
    caching              = "ReadWrite"
    storage_account_type = "Standard_LRS"
  }

  source_image_reference {
    publisher = "RedHat"
    offer     = "RHEL"
    sku       = "87-gen2"
    version   = "latest"
  }
}

# Create Network Security Group and rule
resource "azurerm_network_security_group" "omm_dev_monitor_nsg" {
  name                = "omm-dev-monitor-nsg"
  location            = azurerm_resource_group.omm_dev_monitor_resource_group.location
  resource_group_name = azurerm_resource_group.omm_dev_monitor_resource_group.name

  security_rule {
    name                       = "SSH"
    priority                   = 1001
    direction                  = "Inbound"
    access                     = "Allow"
    protocol                   = "Tcp"
    source_port_range          = "*"
    destination_port_range     = "22"
    source_address_prefix      = "*"
    destination_address_prefix = "*"
  }
}

# Connect the security group to the network interface
resource "azurerm_network_interface_security_group_association" "gis_nic_nsg" {
  network_interface_id      = azurerm_network_interface.omm_dev_network_interface.id
  network_security_group_id = azurerm_network_security_group.omm_dev_monitor_nsg.id
}

resource "azurerm_network_interface_security_group_association" "grds_nic_nsg" {
  network_interface_id      = azurerm_network_interface.omm_dev_grds_vm_01_network_interface.id
  network_security_group_id = azurerm_network_security_group.omm_dev_monitor_nsg.id
}


resource "azurerm_log_analytics_workspace" "omm_dev_log_alalytics_ws" {
  name                = "omm-dev-log-alalytics-ws"
  location            = azurerm_resource_group.omm_dev_monitor_resource_group.location
  resource_group_name = azurerm_resource_group.omm_dev_monitor_resource_group.name
  sku                 = "PerGB2018"
  retention_in_days   = 30
}

resource "azurerm_monitor_data_collection_endpoint" "omm_dev_monitor_dce" {
  name                          = "ommdevmonitordce"
  resource_group_name           = azurerm_resource_group.omm_dev_monitor_resource_group.name
  location                      = azurerm_resource_group.omm_dev_monitor_resource_group.location
  kind                          = "Linux"
  public_network_access_enabled = true
  description                   = "azurerm_monitor_data_collection_endpoint omm_dev_monitor_dce"
  tags = {
    environment = "OMDEV"
  }
}


resource "azapi_resource" "data_collection_logs_table" {
  name      = "CustomLogsTable_CL"
  parent_id = azurerm_log_analytics_workspace.omm_dev_log_alalytics_ws.id
  type      = "Microsoft.OperationalInsights/workspaces/tables@2022-10-01"
  body = jsonencode(
    {
      "properties" : {
        "schema" : {
          "name" : "CustomLogsTable_CL",
          "columns" : [
            {
              "name" : "TimeGenerated",
              "type" : "datetime",
              "description" : "The time at which the data was generated"
            },
            {
              "name" : "RawData",
              "type" : "string",
              "description" : "RawData"
            },
            {
              "name" : "FilePath",
              "type" : "string",
              "description" : "FilePath"
            }
          ]
        },
        "retentionInDays" : 30,
        "totalRetentionInDays" : 30
      }
    }
  )
}


resource "azurerm_monitor_data_collection_rule" "omm_dev_monitor_dcr" {
  name                        = "omm-dev-monitor-dcr"
  resource_group_name         = azurerm_resource_group.omm_dev_monitor_resource_group.name
  location                    = azurerm_resource_group.omm_dev_monitor_resource_group.location
  data_collection_endpoint_id = azurerm_monitor_data_collection_endpoint.omm_dev_monitor_dce.id


  data_sources {
    log_file {
      name          = "logfile"
      format        = "text"
      streams       = ["Custom-${azapi_resource.data_collection_logs_table.name}"]
      file_patterns = ["/omdev/log/gis/${azurerm_linux_virtual_machine.gis_vm_01.name}/GIS-omdev*.log", "/omdev/log/grds/${azurerm_linux_virtual_machine.grds_vm_01.name}/RDS-omdev*.log"]
      settings {
        text {
          record_start_timestamp_format = "ISO 8601"
        }
      }
    }
  }
  destinations {
    log_analytics {
      name                  = azurerm_log_analytics_workspace.omm_dev_log_alalytics_ws.name
      workspace_resource_id = azurerm_log_analytics_workspace.omm_dev_log_alalytics_ws.id
    }
  }
  data_flow {
    streams       = ["Custom-${azapi_resource.data_collection_logs_table.name}"]
    destinations  = [azurerm_log_analytics_workspace.omm_dev_log_alalytics_ws.name]
    output_stream = "Custom-${azapi_resource.data_collection_logs_table.name}"
  }
  stream_declaration {
    stream_name = "Custom-${azapi_resource.data_collection_logs_table.name}"
    column {
      name = "TimeGenerated"
      type = "datetime"
    }
    column {
      name = "RawData"
      type = "string"
    }
    column {
      name = "FilePath"
      type = "string"
    }
  }
}

resource "azurerm_virtual_machine_extension" "omm_dev_ama_gis_01" {
  name                       = "AzureMonitorLinuxAgentGIS"
  virtual_machine_id         = azurerm_linux_virtual_machine.gis_vm_01.id
  publisher                  = "Microsoft.Azure.Monitor"
  type                       = "AzureMonitorLinuxAgent"
  type_handler_version       = "1.6"
}

resource "azurerm_virtual_machine_extension" "omm_dev_ama_grds_01" {
  name                       = "AzureMonitorLinuxAgentGRDS"
  virtual_machine_id         = azurerm_linux_virtual_machine.grds_vm_01.id
  publisher                  = "Microsoft.Azure.Monitor"
  type                       = "AzureMonitorLinuxAgent"
  type_handler_version       = "1.6"
}

resource "azurerm_monitor_data_collection_rule_association" "gis_dcr_association" {
  name                    = "gis-dcr-association"
  target_resource_id      = azurerm_linux_virtual_machine.gis_vm_01.id
  data_collection_rule_id = azurerm_monitor_data_collection_rule.omm_dev_monitor_dcr.id
}

resource "azurerm_monitor_data_collection_rule_association" "grds_dcr_association" {
  name                    = "grds-dcr-association"
  target_resource_id      = azurerm_linux_virtual_machine.grds_vm_01.id
  data_collection_rule_id = azurerm_monitor_data_collection_rule.omm_dev_monitor_dcr.id
}