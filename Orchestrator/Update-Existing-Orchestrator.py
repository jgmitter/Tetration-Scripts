
import sys
from tetpyclient import RestClient
from pprint import pprint
from datetime import datetime
import requests.packages.urllib3
from datetime import datetime
import json


API_ENDPOINT= "https://x.x.x.x"

# Class Constructor
restclient = RestClient(API_ENDPOINT,
                        credentials_file='/Users/jgmitter/Downloads/Tetration-Scripts/TETRATION/credentials.json',
                        verify=False)

requests.packages.urllib3.disable_warnings()


req_payload = {
    "name": "vcenter-name",
    "type": "vCenter",
    "hosts_list": [ { "host_name": "x.x.x.x", "port_number": 443}],
    "username":"administrator@vsphere.local",
    "password":"password"
}

#enter orchestrator id which you can get from get-orchestrator
resp = restclient.put('/orchestrator/Default/5a025dcb497d4f4dd8bd6092', json_body=json.dumps(req_payload))
print resp.status_code
