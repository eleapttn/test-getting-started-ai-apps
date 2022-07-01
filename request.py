import requests
import json

url = 'http://0.0.0.0:5000/'
#url = "https://fafaf666-4c5e-4a40-ac35-f73f111630e0.app.gra.training.ai.cloud.ovh.net"

data = "Elea"
j_data = json.dumps(data)
headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
r = requests.post(url, data=j_data, headers=headers)

print(r.status_code)
print(r.text)