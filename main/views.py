from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

# Create your views here.


def home(request: HttpRequest) -> HttpResponse:
    return render(request, 'main/home.html', {'title': 'Home'})
