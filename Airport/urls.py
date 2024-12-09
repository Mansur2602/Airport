from django.contrib import admin
from django.urls import path
from .views import view_data, create_airport, create_plane, create_travel, create_flight

urlpatterns = [
    path('', view_data, name='view_data'),
    path('create_airport/', create_airport, name='create_airport'),
    path('create_plane/', create_plane, name='create_plane'),
    path('create_travel/', create_travel, name='create_travel'),
    path('create_flight/', create_flight, name='create_flight'),
]
