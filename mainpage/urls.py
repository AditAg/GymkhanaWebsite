from django.conf.urls import url
from . import views

app_name='mainpage'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^contact/$',views.contact,name='contact'),
    url(r'^contact/add/$',views.ContactsCreate,name='contact-add'),
    url(r'^register/$', views.UserFormView.as_view(), name='register'),
    url(r'^login/$',views.Login,name='login'),
    url(r'^logout/$',views.Logout,name='logout'),
    url(r'^eventregister/$',views.UsereventsCreate,name='eventregister'),
    url(r'^eventadd/$',views.Eventadd,name='eventadd'),
    url(r'^(?P<string>[a-zA-Z0-9+=/]+)/verify/$',views.UserVerify,name='userverify'),
    url(r'^chat/$',views.chat,name='chat'),





]
