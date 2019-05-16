from django.contrib import admin
from .models import Music

class MusicAdmin(admin.ModelAdmin):
    list_display = [fields.name for fields in Music._meta.fields]

    class Meta:
        model=Music

admin.site.register(Music,MusicAdmin)
