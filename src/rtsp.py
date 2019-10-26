import requests
import json
import time

device_id = '19151543448'
api_url = 'https://iot.cht.com.tw/iot/v1/device/{0}/snapshot'.format(device_id)

headers = {
    'CK': 'PKYMWHKYFR1ZK2K0YE'}

files = {
    'meta': (None, json.dumps({"id": "camera1", "value": ["carTest"]}),
             'application/json'),
    'file': ('test-image', open('./img/car.jpg', 'rb'), 'image/jpeg')}

response = requests.post(api_url, files=files, headers=headers)
print(response.text.encode('ascii'))


