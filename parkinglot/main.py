from flask import Flask, render_template, jsonify
import requests
import json

app = Flask(__name__)


def getParkUpdate():
    deviceID = "19151543448"
    sensorID = "camera1"
    apiURL = 'https://iot.cht.com.tw/iot/v1/device/{0}/sensor/{1}/snapshot'.format(deviceID, sensorID)
    headers = {
        "CK": "PKYMWHKYFR1ZK2K0YE",
        "device_id": deviceID,
        "sensor_id": sensorID,
        "snapshot_id": "410d8721-cec0-454e-9f7b-f14fade2b938"
    }
    response = requests.get(apiURL, headers=headers)
    picPathUrl = 'testpic.jpg'
    with open(picPathUrl, 'wb') as f:
        f.write(response.content)

    apiURL = 'https://iot.cht.com.tw/apis/CHTIoT/ivs-vehicle/v1/snapshot'
    headers = {
        "X-API-KEY": "ea522b8e-696e-4084-b9eb-97fdbd677d52",
    }

    files = {"file": open(picPathUrl, "rb")}

    response = requests.post(apiURL, files=files, headers=headers)

    return response.text


def controlPark():
    deviceID = "19151543448"
    apiURL = 'https://iot.cht.com.tw/iot/v1/device/{0}/rawdata'.format(deviceID)
    headers = {
        "CK": "PKYMWHKYFR1ZK2K0YE",
        "device_id": deviceID
    }
    response = requests.post(apiURL, headers=headers)


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
    carInfo = json.loads(getParkUpdate())
    carNum = len(carInfo)
    return render_template('index.html', carInfo=carInfo, carNum=carNum)


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/parking')
def parking():
    lotsInfo = json.loads(getParkStatus())
    print(lotsInfo['value'][0])

    return render_template('parking.html', lotsInfo=lotsInfo)


@app.route('/getData', methods=['GET'])
def getData():
    carInfo = json.loads(getParkUpdate())
    carNum = len(carInfo)
    return jsonify(carInfo=carInfo, carNum=carNum)


@app.route('/getLotsData', methods=['GET'])
def getLotsData():
    lotsInfo = json.loads(getParkStatus())
    return jsonify(lotsInfo=lotsInfo)


if __name__ == '__main__':
    app.run(debug=True)
