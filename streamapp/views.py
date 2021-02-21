from django.shortcuts import render
from django.http.response import StreamingHttpResponse
from streamapp.camera import ipcam

def stream(request): 
    return render(request, 'streamapp/stream.html')

def generate(cam):
    while True:
        frame=cam.getframe()
        yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

def ipfeed(request):
    return StreamingHttpResponse(generate(ipcam()),content_type='multipart/x-mixed-replace; boundary=frame')