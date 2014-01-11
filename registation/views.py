from django.contrib import auth
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import redirect_to_login
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.views.generic import CreateView, UpdateView
from companions.models import Route


def register(request):
    User.objects.create_user(request.POST['login'],request.POST['email'],request.POST['pass'])


class CreateUser(CreateView):
    model = User
    success_url = '/'
    #fields = ['username','email','password']
    form_class = UserCreationForm
    def form_valid(self, form):
        instance = form.save()
        user = authenticate(username=instance.username, password=instance.password)
        login(self.request,user)
        return redirect_to_login
