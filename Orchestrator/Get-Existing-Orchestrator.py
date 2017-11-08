
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



resp = restclient.get('/orchestrator/Default')
print resp.status_code
if resp.status_code == 200:
    parsed_resp = json.loads(resp.content)
    print json.dumps(parsed_resp, indent=4, sort_keys=True)
