from django.contrib import admin
from django.urls import path,include
from mask import views as mv

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('streamapp.urls')),
    path('mask/', mv.maskview)
]
