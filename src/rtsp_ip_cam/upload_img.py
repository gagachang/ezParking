import json
import time

import requests


class UploadImg:
    def __init__(self):
        self._device_id = '19151543448'
        self._api_url = 'https://iot.cht.com.tw/iot/v1/device/{0}/snapshot'.format(self._device_id)
        self._img_path = '../../static/img/'
        self._headers = {'CK': 'PKYMWHKYFR1ZK2K0YE'}

    def _get_new_sensor(self):
        return 'camera1'

    def post(self, file_name, description=''):
        try:
            file_name = file_name.replace('.jpg', '')
            files = {
                'meta': (None,
                         json.dumps({'id': self._get_new_sensor(), 'value': [description]}),
                         'application/json'),
                'file': ('test-image',
                          open('{0}{1}.jpg'.format(self._img_path, file_name), 'rb'),
                         'image/jpeg')
            }
            r = requests.post(self._api_url, files=files, headers=self._headers)
            json_data = json.loads(r.text)
            if r.status_code == 200:
                return (json_data['time'], json_data['value'][0])
            else:
                return None
        except Exception:
            return None

if __name__ == '__main__':
    post_img = UploadImg()
    print(post_img.post('car.jpg'))


