from rtsp_ip_cam.upload_img import UploadImg
from vehicle_recognition.upload_result import UploadResult
import threading
import os

if __name__ == '__main__':
    os.chdir('vehicle_recognition')    # cd to sub folder to keep path correct
    uploader_img = UploadImg()
    uploader_result = UploadResult()

    threading.Thread(target=uploader_img.keep_post_img).start()
    threading.Thread(target=uploader_result.keep_post_result).start()
