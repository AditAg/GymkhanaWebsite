from django.db import models
from django.core.urlresolvers import reverse
from chat_app.models import Profile
from django.contrib.auth.models import User

# Create your models here.


class LatestNews(models.Model):
    news_image = models.CharField(max_length=1000)
    news_text = models.CharField(max_length=1000)
    news_title = models.CharField(max_length=500)

    def __str__(self):
        return self.news_title


class Events(models.Model):
    event_title = models.CharField(max_length=500)
    event_detail = models.CharField(max_length=1000)
    event_date = models.CharField(max_length=250)
    event_url=models.CharField(max_length=300,default="")

    def __str__(self):
        return self.event_title


class Contacts(models.Model):
    contact_name=models.CharField(max_length=100)
    contact_email=models.CharField(max_length=200)
    contact_phone=models.CharField(max_length=30)
    contact_message=models.CharField(max_length=1000)
    def __str__(self):
        return self.contact_name

    def get_absolute_url(self):
        return reverse('mainpage:contact',kwargs={})

class Userevents(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    event_title = models.CharField(max_length=500)
    event_detail = models.CharField(max_length=1000)
    event_date = models.CharField(max_length=250)
    event_url=models.CharField(max_length=300,default="")

    def __str__(self):
        return self.event_title

    def get_absolute_url(self):
        return reverse('mainpage:index',kwargs={})

#Rem:Use base template for the pages of clubs and councils.

