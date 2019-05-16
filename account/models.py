from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class Profile(models.Model):

    user=models.OneToOneField(settings.AUTH_USER_MODEL)
    image=models.ImageField(upload_to='media/image')


class Messages(models.Model):

    text = models.TextField(verbose_name="Текст сообщения")
    sender = models.ForeignKey(User, default = None, blank=True, null=True, verbose_name='Отправитель')
    date = models.DateTimeField(auto_now_add=True, auto_now=False)
    id = models.AutoField(primary_key=True)
