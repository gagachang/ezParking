from flask import Flask, render_template, jsonify
import requests
import json

app = Flask(__name__)


# def getParkUpdate():
#     deviceID = "19151543448"
#     sensorID = "camera1"
#     apiURL = 'https://iot.cht.com.tw/iot/v1/device/{0}/sensor/{1}/snapshot'.format(deviceID, sensorID)
#     headers = {
#         "CK": "PKYMWHKYFR1ZK2K0YE",
#         "device_id": deviceID,
#         "sensor_id": sensorID
#     }
#     response = requests.get(apiURL, headers=headers)
#     picPathUrl = 'images.jpg'
#     with open(picPathUrl, 'wb') as f:
#         f.write(response.content)
#
#     apiURL = 'https://iot.cht.com.tw/apis/CHTIoT/ivs-vehicle/v1/snapshot'
#     headers = {
#         "X-API-KEY": "ea522b8e-696e-4084-b9eb-97fdbd677d52",
#     }
#
#     files = {"file": open(picPathUrl, "rb")}
#
#     response = requests.post(apiURL, files=files, headers=headers)
#
#     return response.text


def getResultPic():
    deviceID = "19151543448"
    sensorID = "recogResult1"
    apiURL = 'https://iot.cht.com.tw/iot/v1/device/{0}/sensor/{1}/snapshot'.format(deviceID, sensorID)
    headers = {
        "CK": "PKYMWHKYFR1ZK2K0YE",
        "device_id": deviceID,
        "sensor_id": sensorID
    }
    response = requests.get(apiURL, headers=headers)
    picPathUrl = 'static/images/result.jpg'
    with open(picPathUrl, 'wb') as f:
        f.write(response.content)


def getResultMeta():
    deviceID = "19151543448"
    sensorID = "recogResult1"
    apiURL = 'https://iot.cht.com.tw/iot/v1/device/{0}/sensor/{1}/snapshot/meta'.format(deviceID, sensorID)
    headers = {
        "CK": "PKYMWHKYFR1ZK2K0YE",
        "device_id": deviceID,
        "sensor_id": sensorID
    }
    response = requests.get(apiURL, headers=headers)
    return response.text


def getParkStatus():
    deviceID = "19151543448"
    sensorID = "parkingStatus1"
    apiURL = 'https://iot.cht.com.tw/iot/v1/device/{0}/sensor/{1}/rawdata'.format(deviceID, sensorID)
    headers = {
        "CK": "PKYMWHKYFR1ZK2K0YE",
        "device_id": deviceID,
        "sensor_id": sensorID
    }
    response = requests.get(apiURL, headers=headers)
    return response.text


@app.route('/')
def home():
    # carInfo = json.loads(getParkUpdate())
    # carNum = len(carInfo)
    return render_template('index.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/parking')
def parking():
    lotsInfo = json.loads(getParkStatus())

    return render_template('parking.html', lotsInfo=lotsInfo)


@app.route('/getRecogData', methods=['GET'])
def getRecogData():
    getResultPic()
    metaInfo = getResultMeta()
    return metaInfo


@app.route('/getLotsData', methods=['GET'])
def getLotsData():
    lotsInfo = json.loads(getParkStatus())
    return jsonify(lotsInfo=lotsInfo)


if __name__ == '__main__':
    app.run(debug=True)
