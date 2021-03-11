"""
ONOS Beispiel
"""
import json
import requests

URL = "http://172.17.0.2:8181/onos/v1/hosts"
CRED = ('onos', 'rocks')

HDR = {'Accept': 'application/json'}

RESP = requests.get(URL, headers=HDR, auth=CRED)

print(RESP.status_code)
RESP_PAYLOAD = RESP.text
print(type(RESP_PAYLOAD))

BODY_JSON = RESP.json()
print(type(BODY_JSON))
for i in BODY_JSON.keys():
    print(i)

print('*'*20)
print(BODY_JSON)
