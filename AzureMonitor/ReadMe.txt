#1.  Connect to VM1(grds)
(base) pawgupta0@WKMZT1D2F51B AzureMonitor % chmod 400 azureuser_ssh_pub_key.pem 

(base) pawgupta0@WKMZT1D2F51B AzureMonitor % ssh -i azureuser_ssh_pub_key.pem  azureuser@135.237.120.82
Activate the web console with: systemctl enable --now cockpit.socket

Register this system with Red Hat Insights: insights-client --register
Create an account or view all your systems at https://red.ht/insights-dashboard
[azureuser@app-vm ~]$ 


#2. Install python

[azureuser@app-vm ~]$ sudo yum install python3.11



#3. Split log row to column
omm-dev-log-grds-dcr

omm-dev-log-grds-detail-dcr
omm_dev_log_detail_table_CL


/omdev/log/grds/app-vm/RDS-omdev*.log

source | project d = split(RawData,"|") | project TimeGenerated=todatetime(d[0]), LoggerName=tostring(d[1]), ThreadName=tostring(d[2]), LogLevel=tostring(d[3]), Message=tostring(d[4])

source | project d = split(RawData,"|") | project TimeGenerated=datetime(2007-11-01), LoggerName=tostring(d[1]), ThreadName=tostring(d[2]), LogLevel=tostring(d[3]), Message=tostring(d[4])

source 
    | project d = split(RawData,"|") 
    | project TimeGenerated=datetime(2007-11-01), LoggerName=tostring(d[1]), ThreadName=tostring(d[2]), LogLevel=tostring(d[3]), Message=tostring(d[4]), AppName=tostring("CORE-GRDS"), HostName=tostring("GRDS-VM-01")

#4. Connect to VM2 (GIS)

omm-dev-log-gis-detail-dcr

/omdev/log/gis/app-gis-vm/GIS-omdev*.log

omm_dev_log_detail_table_pipe_CL_CL

source 
    | project d = split(RawData,"|") 
    | project TimeGenerated=datetime(2007-11-01), LoggerName=tostring(d[1]), ThreadName=tostring(d[2]), LogLevel=tostring(d[3]), Message=tostring(d[4]), AppName=tostring("CORE-GIS"), HostName=tostring("GIS-VM-01")


ssh -i azureuser_ssh_pub_key.pem  azureuser@20.51.192.76