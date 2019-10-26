import os
import time
from datetime import datetime

import rtsp


class IPCam:
    def __init__(self, img_path=None):
        self._rtsp_url = 'rtsp://192.168.0.4:8554/live'
        self._img_path = img_path or '../../static/img/record/'
        self._rtsp_client = rtsp.Client(self._rtsp_url)

    def record_img(self):
        try:
            record_path = '{0}{1}.jpg'.format(
                self._img_path, datetime.now().strftime("%Y%m%d-%H%M%S"))
            self._rtsp_client.read().save(record_path)
            return os.path.basename(record_path)
        except Exception as e:
            print(e)
            return None

    def keep_record_img(self, interval=10):
        assert interval >= 10, 'Time interval should >= 10 secs'
        while True:
            begin = time.time()
            print(self.record_img())
            time.sleep(max(0.0, interval-(time.time()-begin)))


if __name__ == '__main__':
    ip_cam = IPCam()
    while True:
        print(ip_cam.keep_record_img())
