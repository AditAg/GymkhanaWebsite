from django.conf.urls import url
from . import views

app_name='userrelated'
urlpatterns=[
    url(r'^$',views.userspecific,name="userspecific")
]