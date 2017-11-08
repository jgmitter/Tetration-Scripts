
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
    "username":"admin",
    "password":"Pasword"
}
resp = restclient.post('/orchestrator/Default', json_body=json.dumps(req_payload))
print resp.status_code
