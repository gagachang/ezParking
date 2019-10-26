import json
import time

import requests

from rtsp_ip_cam.record_img import IPCam


class UploadImg:
    def __init__(self):
        self._device_id = '19151543448'
        self._sensor_id = 'camera1'
        self._api_url = ('https://iot.cht.com.tw/iot/v1'
                         '/device/{0}/snapshot'.format(self._device_id))
        self._img_path = '../../static/img/record/'
        self._headers = {'CK': 'PKYMWHKYFR1ZK2K0YE'}

    def post_img(self, file_name, description=''):
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

    def keep_post_img(self, interval=10):
        assert interval >= 10, 'Time interval should >= 10 secs'
        ip_cam = IPCam()
        while True:
            begin = time.time()
            print(self.post_img(ip_cam.record_img()))
            time.sleep(max(0.0, interval-(time.time()-begin)))


if __name__ == '__main__':
    uploader = UploadImg()
    uploader.keep_post_img()
