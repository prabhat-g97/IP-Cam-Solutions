from django.urls import path
from streamapp import views

urlpatterns = [
    path('stream/', views.stream, name='stream'),
    path('ipfeed', views.ipfeed, name='ipfeed')
]
    