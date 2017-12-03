from django.db import models
from django.contrib.auth.models import User

class Emailmessage(models.Model):
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    From = models.CharField(max_length=255)
    To = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.CharField(max_length=1000)

