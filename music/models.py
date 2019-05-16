from django.db import models

class Music(models.Model):
    artist = models.CharField("Artist",max_length=50)
    title = models.CharField("Title",max_length=50)
    upload = models.FileField("Upload your file", upload_to='media/music')
    date = models.DateField(auto_now_add=True)