from email.policy import default
from django.db import models
from datetime import datetime
# Create your models here.
class Room(models.Model):
  room_name = models.CharField(max_length=1000000)

class Message(models.Model):
  user_id = models.CharField(max_length=1000000)
  room_name = models.CharField(max_length=1000000)
  date = models.DateTimeField(default=datetime.now,blank=True)
  msg = models.CharField(max_length=10000000000)
