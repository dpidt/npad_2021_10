import requests
import json
from pprint import pprint

ONOS_IP = '172.17.0.2'
ONOS_USER = 'onos'
ONOS_PW = 'rocks'

onos_login = (ONOS_USER, ONOS_PW)
base_url = 'http://{}:8181/onos/v1'.format(ONOS_IP)
get_hdr = {'accept': 'application/json'}
post_hdr = {'accept': 'application/json',
            'content-type': 'application/json'}

hosts_uri = '/hosts'
hosts_url = base_url + hosts_uri
host_response = requests.get(hosts_url, auth=onos_login, headers=get_hdr)
print(host_response.status_code)
if str(host_response.status_code).startswith('2'):
    body = host_response.json()
    pprint(body, indent=4)
    one = {'ip': '255.255.255.255', 'id': '00:00:00:00:00:00/None'}
    two = {'ip': '0.0.0.0', 'id': '00:00:00:00:00:00/None'}
    for host in body['hosts']:
        pprint(host, indent=4)
        if host['ipAddresses'][0] < one['ip']:
            one['ip'] = host['ipAddresses'][0]
            one['id'] = host['id']
        if host['ipAddresses'][0] > two['ip']:
            two['ip'] = host['ipAddresses'][0]
            two['id'] = host['id']

    print(one)
    print(two)

intent_uri = '/intents'
intent_url = base_url+intent_uri
intent_data = {'type': 'HostToHostIntent',
               'appId': 'org.onosproject.ovsdb',
               'priority': 55,
               'one': one['id'],
               'two': two['id']}
pprint(intent_data, indent=4)
intent_response = requests.post(intent_url, auth=onos_login, headers=post_hdr,
                                data=json.dumps(intent_data))
print(intent_response.status_code)
