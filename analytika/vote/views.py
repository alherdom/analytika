from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

def votes(request: HttpRequest) -> HttpResponse:
    return render(request, "vote/votes.html")
