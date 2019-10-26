import json
import time

import cv2
import requests

from vehicle_recognition.download_img import DownloadImg
from vehicle_recognition.recognize_vehicle import RecognizeVehicle


class UploadResult:
    def __init__(self):
        self._device_id = '19151543448'
        self._sensor_id = 'recogResult1'
        self._api_url = ('https://iot.cht.com.tw/iot/v1'
                         '/device/{0}/snapshot'.format(self._device_id))
        self._img_path = '../../static/img/result/'
        self._headers = {'CK': 'PKYMWHKYFR1ZK2K0YE'}

    def _post_result(self, file_name, description=''):
        try:
            file_name = file_name.replace('.jpg', '')
            files = {
                'meta': (None,
                         json.dumps({'id': self._sensor_id,
                                     'value': [description]}),
                         'application/json'),
                'file': ('test-image',
                         open('{0}{1}.jpg'.format(self._img_path, file_name),
                              'rb'),
                         'image/jpeg')
            }
            r = requests.post(self._api_url, files=files,
                              headers=self._headers)
            json_data = json.loads(r.text)
            if r.status_code == 200:
                return json_data['time'], json_data['value'][0]
            else:
                return None
        except Exception as e:
            print(e)
            return None

    def keep_post_result(self, interval=10):
        downloader = DownloadImg()
        recognizer = RecognizeVehicle()
        while True:
            begin = time.time()
            file_name = downloader.get_img()
            result = recognizer.recognize(file_name)
            labeler = _LabelVehicle(file_name)
            labeler.label(result)
            print(self._post_result(file_name))
            time.sleep(max(0.0, interval-(time.time()-begin)))


class _LabelVehicle:
    def __init__(self, file_name):
        self._img_path = '../../static/img/download/'
        self._result_path = self._img_path.replace('download', 'result')
        self._file_name = file_name
        self._color = (255, 0, 0)
        self._thickness = 10

    def label(self, recognize_result):
        try:
            image = cv2.imread('{0}{1}'.format(
                self._img_path, self._file_name))

            for vehicle in recognize_result:
                start_point = (vehicle['x'], vehicle['y'])
                end_point = (vehicle['x'] + vehicle['width'],
                             vehicle['y'] + vehicle['height'])
                image = cv2.rectangle(image, start_point, end_point,
                                      self._color, self._thickness)

            cv2.imwrite('{0}{1}'.format(self._result_path, self._file_name),
                        image)
            return self._file_name
        except Exception as e:
            print(e)
            return None


if __name__ == '__main__':
    uploader = UploadResult()
    uploader.keep_post_result()

