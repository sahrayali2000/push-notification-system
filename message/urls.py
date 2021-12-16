from django.urls import path, include
from .views import *
app_name = 'message'
urlpatterns = [
    path('service-worker.js', service_worker, name='service-worker'),
    path('', index, name='index'),
    path('send-notification/', notif_send, name='notif-send'),
]