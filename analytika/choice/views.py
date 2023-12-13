from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import Choice

def choices(request: HttpRequest, poll: str ) -> HttpResponse:
    choices = Choice.objects.filter(poll=poll)
    return render(request, "choice/choices.html", dict(choices=choices))
