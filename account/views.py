from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login, update_session_auth_hash
from django.http import HttpResponseRedirect
from django.views.generic.base import View
from django.contrib.auth import logout
from django.contrib import messages
from .forms import sendForm
from django.http import HttpResponse
from .models import Messages
from music.models import Music


class RegisterFormView(FormView):
    form_class = UserCreationForm
    success_url = "/account/login"
    template_name = "registration.html"
    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)


class LoginFormView(FormView):
    form_class = AuthenticationForm
    template_name = "login.html"
    success_url = "/"

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect("/")


def ChangePasswordView(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {
        'form': form
    })


def home(request):
    form = sendForm
    last = Music.objects.last()
    musics = Music.objects.filter(id__gte=last.id - 20)
    return render(request, 'home.html', locals())


def send_msg(request):
    if request.method == 'GET':
        txt = request.GET.get('text')
        msg = Messages(text=txt, sender=request.user)
        msg.save()

    return HttpResponse('')


def ajax_comments(request):
    if request.method == 'GET':
        last = Music.objects.last()
        msg_set = Messages.objects.filter(id__gte=last.id-50)
        resp = ''
        odd = True
        for msg in msg_set:
            resp += '<div class="Message-'
            if odd:
                resp += '1'
                odd = False
            else:
                resp += '2'
                odd = True
            resp += '"><span class="author">'
            if msg.sender:
                resp += msg.sender.username
            resp += '<span>'
            # text = str(msg.date)
            # date = re.search(r'')
            resp += '<span class="date">' + str(msg.date) + '</span>'
            resp += '<p>' + msg.text + '</p>'
            resp += '</div>'
        return HttpResponse(resp, content_type='text/html')


def search(request):
    if request.GET:
        text = request.GET.get('text')
        music_set = Music.objects.filter(title__contains=text)
        if len(music_set) == 0:
            resp = 'Нет аудиозаписей, удовлетворяющих условия поиска'
        else:
            resp = ''
            for music in music_set:
                resp += '<li><a href="#" data-src="static/media/' + str(music.upload) + '">' + str(music.title) + '</a></li>'

                print(resp)
    return HttpResponse(resp, content_type='text/html')