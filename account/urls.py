from . import views
from django.conf.urls import url

urlpatterns=[
    url(r'^$', views.home, name='home'),
    url(r'^registration/$', views.RegisterFormView.as_view(), name='registration'),
    url(r'^login/$', views.LoginFormView.as_view(), name='login'),
    url(r'^logout/$', views.LogoutView.as_view(), name='logout'),
    url(r'^password/$', views.ChangePasswordView, name='change_password'),
    url(r'^ajax_comments/$', views.ajax_comments, name='ajax_comments'),
    url(r'^send_msg/$', views.send_msg, name='send_msg'),
    url(r'^search/$', views.search, name='search'),
]