from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http.request import HttpHeaders
from pusher_push_notifications import PushNotifications
from django.views.decorators.csrf import csrf_exempt
from pusher import Pusher
from .models import *
from django.http import JsonResponse, HttpResponse
import requests
from django.contrib import messages

import json
# Create your views here.



def index(request):
    return render(request, 'message/index.html', {})


def service_worker(request):
     with open('message/templates/message/service-worker.js') as f:
          return HttpResponse(f, content_type='text/javascript')


def send_notif(message_title, message_body, message_link='#'):
     beams_client = PushNotifications(
          instance_id='32876e2b-5337-41b3-a3fe-70be471f5e5c',
          secret_key='C23A835C45215D784A20E6F11B900418B7E33096B5D73BF2879C6AD4A3DF933C',
     )

     response = beams_client.publish_to_interests(
          interests=['hello'],
          publish_body={
               'web': {
                    'notification': {
                         'title': f'{message_title}',
                         'body': f'{message_body}',
                         'deep_link': f'http://{message_link}',
                    },
               },
          },
     )

     print(response['publishId'])


def notif_send(request):
     if request.method == 'POST':
          title = request.POST['title']
          body = request.POST['body']
          link = request.POST['link']
          send_notif(title, body, link)
          messages.success(request, 'notification sent!')
          return render(request, 'message/send-notification.html', context={})

     return render(request, 'message/send-notification.html', context={})