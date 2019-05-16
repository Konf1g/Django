from django.shortcuts import render
from .forms import musicForm
from .models import Music

def upload(request):
        form = musicForm(request.POST, request.FILES or None)
        if request.method == "POST" and form.is_valid() and request.FILES:
            upload = form.cleaned_data
            form.save()
        mus_set = Music.objects.all()
        for music in mus_set:
            print(music.upload)
        return render(request, 'upload.html', locals())


