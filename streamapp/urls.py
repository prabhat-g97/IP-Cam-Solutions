from django.urls import path
from streamapp import views

urlpatterns = [
    path('stream', views.main, name='home'),
    path('feed', views.feed, name='feed')
]
