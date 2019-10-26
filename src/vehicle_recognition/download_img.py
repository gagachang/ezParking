import os
from datetime import datetime

import requests


class DownloadImg:
    def __init__(self):
        self._device_id = '19151543448'
        self._sensor_id = 'camera1'
        self._api_url = ('https://iot.cht.com.tw/iot/v1'
                         '/device/{0}/sensor/{1}/snapshot'.format(
                             self._device_id, self._sensor_id))
        self._img_path = '../../static/img/download/'
        self._headers = {'CK': 'PKYMWHKYFR1ZK2K0YE',
                         'device_id': self._device_id,
                         'sensor_id': self._sensor_id}

    def get_img(self):
        try:
            r = requests.get(self._api_url, headers=self._headers)
            if r.status_code == 200:
                download_path = '{0}{1}.jpg'.format(
                    self._img_path, datetime.now().strftime('%Y%m%d-%H%M%S'))
                with open(download_path, 'wb') as wf:
                    wf.write(r.content)
                return os.path.basename(download_path)
            else:
                return None
        except Exception as e:
            print(e)
            return None


if __name__ == '__main__':
    downloader = DownloadImg()
    print(downloader.get_img())
