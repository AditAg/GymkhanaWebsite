from django.conf.urls import url
from . import views

app_name='chat_app'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.Login, name='Login'),
    url(r'^logout/$', views.Logout, name='Logout'),
    url(r'^new/$', views.ChatroomCreate.as_view(), name='new_room'),
    url(r'^(?P<label>[\w-]{,50})/$', views.chat_room, name='chat_room'),
    url(r'^(?P<label>[\w-]{,50})/post/$', views.Post, name='Post'),
    url(r'^(?P<label>[\w-]{,50})/messages/$', views.Messages, name='Messages'),
    url(r'^(?P<label>[\w-]{,50})/home/$', views.Home, name='Home'),
    #url(r'^(?P<chat_room_id>[0-9]+)/$', views.chat_room, name='chat_room'),
]
