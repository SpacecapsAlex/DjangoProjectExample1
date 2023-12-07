from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from .models import User

# Create your views here.


def list_users(request: HttpRequest) -> HttpResponse:
    return render(request, 'users/list_users.html', {'users': User.objects.all()})
