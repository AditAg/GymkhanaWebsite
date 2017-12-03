from django.contrib import admin
from .models import Councils,Clubs,Clubevents,Achievements,Clubgallery

# Register your models here.
admin.site.register(Councils)
admin.site.register(Clubs)
admin.site.register(Clubevents)
admin.site.register(Clubgallery)
admin.site.register(Achievements)