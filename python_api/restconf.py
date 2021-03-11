import requests

url = "http://192.168.181.23/restconf/data/ietf-restconf-monitoring:restconf-state/capabilities"

payload={}
headers = {
  'Accept': 'application/yang.data+json',
  'Authorization': 'Basic YWRtaW46Y2lzY28=',
  'Cookie': 'APIC-cookie=rNxeSR3cbNSK1sqKfFSTLa++DB1hFiHBMrqv0cwQn+B9TrWqI5ag7B0vfr1tVcZdjBMqeJqYOibm3TEgO2kkNX48KhLqSLH2AEKpWPedFalcqVFlFPMlKOcJauzdT73NpOOa5RFBLFJC57mWFPTRRtJhuy5Dvl6ysh760BIJxco='
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
print(type(response.json()))
my_resp = response.json()
print(my_resp['capabilities']['capability'])
my_resp['capabilities']['capability'] = 'Feature'
print(my_resp)
