import json
import time

import requests

from vehicle_recognition.download_img import DownloadImg


class RecognizeVehicle:
    def __init__(self):
        self._api_url = ('https://iot.cht.com.tw/apis'
                         '/CHTIoT/ivs-vehicle/v1/snapshot')
        self._img_path = '../../static/img/download/'
        self._headers = {'X-API-KEY': 'ea522b8e-696e-4084-b9eb-97fdbd677d52'}

    def recognize(self, file_name):
        try:
            file_name = file_name.replace('.jpg', '')
            files = {'file': open('{0}{1}.jpg'.format(
                                  self._img_path, file_name), 'rb')}
            r = requests.post(self._api_url,
                              headers=self._headers, files=files)
            json_data = json.loads(r.text)

            if r.status_code == 200:
                return json_data
            else:
                return None
        except Exception as e:
            print(e)
            return None

    def keep_recognize(self, interval=10):
        assert interval >= 10, 'Time interval should >= 10 secs'
        downloader = DownloadImg()
        while True:
            begin = time.time()
            result = self.recognize(downloader.get_img())
            if result is not None:
                print(len(result), result)
            time.sleep(max(0.0, interval-(time.time()-begin)))


if __name__ == '__main__':
    recognizer = RecognizeVehicle()
    recognizer.keep_recognize()
