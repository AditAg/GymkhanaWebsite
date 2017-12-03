from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from django.core.urlresolvers import reverse


#Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Chatroom(models.Model):
    name = models.CharField(max_length=200)
    label= models.SlugField(unique=True,default='1')

    def __unicode__(self):
        return self.label

    def get_absolute_url(self):
        return reverse('chat_app:chat_room',kwargs={'label':self.label})


class Chat(models.Model):
    room = models.ForeignKey(Chatroom,on_delete=models.CASCADE,default='1')
    created = models.DateTimeField(default=timezone.now ,db_index=True )
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    message = models.CharField(max_length=200,default=' ')

    def __unicode__(self):
        return '[{timestamp}] {handle}: {message}'.format(**self.as_dict())

    #this is used so that this function can be used in the HTML template directly and doesn't
    #require a custom template filter(else functions of models can be only used in views
    @property
    def formatted_timestamp(self):
        return self.created.strftime('%b %d %I:%M %p')

    def as_dict(self):
        return {'handle':self.user.username,'message':self.message,'timestamp':self.formatted_timestamp}



        # @receiver(post_save, sender=User)
        # def create_user_profile(sender, instance, created, **kwargs):
        #    if created:
        #        Profile.objects.create(user=instance)

        # @receiver(post_save, sender=User)
        # def save_user_profile(sender, instance, **kwargs):
        #    instance.profile.save()
