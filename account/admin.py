from django.contrib import admin
from .models import *

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user','image']

    class Meta:
        model=Profile


class MessageAdmin(admin.ModelAdmin):
    list_display = ['sender', 'text']

    class Meta:
        model = Messages
# Register your models here.
admin.site.register(Messages, MessageAdmin)
admin.site.register(Profile,ProfileAdmin)
