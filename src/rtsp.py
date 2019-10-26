import requests
import json
import time

# upload picture to sensor
deviceID = '19151543448'
api_url = 'https://iot.cht.com.tw/iot/v1/device/{0}/snapshot'.format(deviceID)

headers = {
    'CK': 'PKYMWHKYFR1ZK2K0YE'}

files = {
    'meta': (None, json.dumps({"id": "camera1", "value": ["carTest"]}),
             'application/json'),
    'file': ('test-image', open('../static/img/car2.jpg', 'rb'), 'image/jpeg')}

response = requests.post(api_url, files=files, headers=headers)
print(response.text.encode('ascii'))

# download picture to raspberry pi2
sensorID = "camera1"
apiURL = 'https://iot.cht.com.tw/iot/v1/device/' + deviceID + '/sensor/' + sensorID + '/snapshot'  # restful url (GET)

headers = {
    "CK": "PKYMWHKYFR1ZK2K0YE",
    "device_id": deviceID,
    "sensor_id": sensorID
}

response = requests.get(apiURL, headers=headers)
with open("../static/img/car1.jpg", 'wb') as f:
    f.write(response.content)

# upload picture to car detection api, then evaluate/upload parking lots information
apiURL = 'https://iot.cht.com.tw/apis/CHTIoT/ivs-vehicle/v1/snapshot'

headers = {
    "X-API-KEY": "ea522b8e-696e-4084-b9eb-97fdbd677d52",
}

files = {"file": open("../static/img/car2.jpg", "rb")}

response = requests.post(apiURL, files=files, headers=headers)
print(response.text)  # Here we get how many cars parking in the camera area
