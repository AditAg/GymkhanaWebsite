from django.contrib import admin
from .models import LatestNews, Events, Contacts,Userevents

# Register your models here.
admin.site.register(LatestNews)
admin.site.register(Events)
admin.site.register(Contacts)
admin.site.register(Userevents)