from django.contrib import admin
from django.urls import path
from tracks.api import api
from tracks.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api.urls), # test, api.py(/upload)
    path('index/', index, name='index') # [views] index
]
