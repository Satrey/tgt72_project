from django.urls import path, include
from .views import login_user, logout_user, main

urlpatterns = [
    path('login/', login_user, name='login_user'),
    path('logout/', logout_user, name='logout_user'),
    path('main/', main, name='main')
]
