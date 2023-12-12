from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Poll


def polls(request: HttpRequest) -> HttpResponse:
    polls = Poll.objects.all()
    return render(request, "polls.html", dict(polls=polls, section="polls"))


def poll_detail(request: HttpRequest, poll_slug: str) -> HttpResponse:
    poll_detail = Poll.objects.get(slug=poll_slug)
    return render(
        request,
        "poll_detail.html",
        dict(poll_detail=poll_detail, section="poll_detail"),
    )
