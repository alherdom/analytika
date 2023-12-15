from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse


# def index(request: HttpRequest) -> HttpResponse:
#     return render(request, "index.html")


def index(request: HttpRequest) -> HttpResponse:
    return redirect("poll:polls")
