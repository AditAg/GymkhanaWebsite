from django.contrib import admin
from .models import Chat,Profile,Chatroom

# Register your models here.

assert isinstance(admin.site.register, object)
admin.site.register(Profile)
admin.site.register(Chat)
admin.site.register(Chatroom)
