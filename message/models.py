from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Conversation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=500, null=True, blank=True)
    status = models.CharField(max_length=500, null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True)
