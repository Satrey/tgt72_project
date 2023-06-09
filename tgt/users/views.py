from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import CustomUser
from .forms import UserAuthForm


def login_user(request):
    if request.method == 'GET':
        return render(request, 'users/login.html', {'form': UserAuthForm})
    else:
        user = authenticate(request, username=request.POST['username'],
                            password=request.POST['password'])
        if user is None:
            return render(request, 'users/login.html', {'form': UserAuthForm(), 
                                                        'error': 'Не верное имя пользователя или пароль'})
        else:
            login(request, user)
            return redirect('main')


@login_required
def logout_user(request):
    logout(request)
    return render(request, 'users/logout.html')


@login_required
def main(request):
    return render(request, 'users/main.html')


class CustomUserListView(ListView):
    model = CustomUser
    template_name = 'users/user_list.html'
    paginate_by = 10


class UserDetailView(DetailView):
    model = CustomUser
    template_name = 'users/user_detail.html'


