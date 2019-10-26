import json
import time

import requests

from rtsp_ip_cam.record_img import IPCam


class UploadExistence:
    def __init__(self):
        self._device_id = '19151543448'
        self._api_url = ('https://iot.cht.com.tw/iot/v1'
                         '/device/{0}/rawdata'.format(self._device_id))
        self._img_path = '../../static/img/record/'
        self._headers = {'CK': 'PKYMWHKYFR1ZK2K0YE',
                         'device_id': self._device_id}
        self._park_status = {'A1': 0, 'A2': 0, 'A3': 0}
        self._data = [{
            'id': 'parkingStatus1',
            'lat': 24.793539, 'lon': 120.991245,
            'save': False, 'value': ['']}]

    def _check_existence(self, result):
        for a in ('A1', 'A2', 'A3'):
            self._park_status[a] = 0
        for vehicle in result:
            middle_x = vehicle['x'] + vehicle['width']//2
            middle_y = vehicle['y'] + vehicle['height']//2

            if 550 <= middle_x <= 790 and 325 <= middle_y <= 435:
                self._park_status['A1'] = 1
            elif 985 <= middle_x <= 1245 and 400 <= middle_y <= 510:
                self._park_status['A2'] = 1
            elif 1420 <= middle_x <= 1690 and 460 <= middle_y <= 580:
                self._park_status['A3'] = 1
        self._data[0]['value'] = [json.dumps(self._park_status)]

    def post_status(self, result):
        try:
            if result is None:
                return None
            self._check_existence(result)
            r = requests.post(self._api_url,
                              headers=self._headers,
                              data=json.dumps(self._data))
            if r.status_code == 200:
                return r.text
            else:
                return None
        except Exception as e:
            print(e)
            return None


if __name__ == '__main__':
    uploader = UploadExistence()
    uploader.post_status(None)
