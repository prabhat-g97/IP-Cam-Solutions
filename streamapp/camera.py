from django.conf import settings
import os, cv2, urllib.request
import numpy as np

class ipcam(object):
    def __init__(self):
        self.url="http://192.168.1.11:8080/shot.jpg"

    def getframe(self):
        imgresp=urllib.request.urlopen(self.url)
        imgbytearray=np.array(bytearray(imgresp.read()),dtype=np.uint8)
        img=cv2.imdecode(imgbytearray,-1)
        resize=cv2.resize(img,(640,480),interpolation=cv2.INTER_LINEAR)
        ret,jpeg=cv2.imencode('.jpg',resize)
        return jpeg.tobytes()