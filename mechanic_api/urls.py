from django.contrib import admin
from django.urls import path, include
from mechanic_api.views.mechanic import add_mechanic, get_mechanics
from mechanic_api.views.requests import add_request
from mechanic_api.views.authentication import login, register


urlpatterns = [
    path('create-mechanic', add_mechanic, name='add_mechanic'),
    path('get-mechanics', get_mechanics, name='get_mechanics'),
    path('create-request', add_request, name='add_request'),
    path('login', login, name='login_user'),
    path('register', register, name='register_user')
]
