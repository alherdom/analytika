from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Poll
from choice.models import Choice


def polls(request: HttpRequest) -> HttpResponse:
    polls = Poll.objects.filter(active=True)
    return render(request, "polls.html", dict(polls=polls))


def poll_vote(request: HttpRequest, poll_slug: str) -> HttpResponse:
    poll = Poll.objects.get(slug=poll_slug)
    choices = Choice.objects.filter(poll=poll)
    return render(
        request,
        "poll_vote.html",
        dict(poll=poll, choices=choices, section="poll-detail"),
    )
