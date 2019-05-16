from . import views
from  django.conf.urls import url
from  django.contrib.auth.views import login

urlpatterns=[
    url(r'^upload/',  views.upload, name="Upload your music"),
]