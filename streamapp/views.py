from django.shortcuts import render
from django.http.response import StreamingHttpResponse
from streamapp.camera import ipwebcam

def main(request): 
    return render(request, 'streamapp/home.html')