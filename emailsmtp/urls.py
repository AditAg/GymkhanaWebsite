from django.conf.urls import url, include
from django.conf import settings
from django.views.generic.base import TemplateView
from . import views

app_name='emailsmtp'
urlpatterns=[
    url(r'^send/$', views.sendmail,name='sendmail'),
    url(r'^sendmail2/$', views.sendmail2,name='sendmail2'),
    url(r'^thankyou/$', TemplateView.as_view(template_name='emailsmtp/thankyou.html'), name='thankyou'),
    #url(r'^$', TemplateView.as_view(template_name='emailsmtp/email.html'), name='email'),
    url(r'^$',views.select,name='select'),
    url(r'^emailform/$',views.emailform,name='emailform'),
    url(r'^emailform2/$',views.emailform2,name='emailform2'),
]
