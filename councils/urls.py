from django.conf.urls import url
from . import views

app_name='councils'
urlpatterns=[
    url(r'^(?P<council_id>[0-9]+)/$',views.index,name="index"),
    url(r'^(?P<council_id>[0-9]+)/(?P<club_id>[0-9]+)/$',views.clubpage,name='clubpage'),
    url(r'^(?P<council_id>[0-9]+)/(?P<club_id>[0-9]+)/gallery/$',views.gallery,name='gallery'),
    url(r'^(?P<council_id>[0-9]+)/(?P<club_id>[0-9]+)/events/$',views.events,name='events'),
    url(r'^(?P<council_id>[0-9]+)/(?P<club_id>[0-9]+)/contacts/$',views.contacts,name='contacts'),
]