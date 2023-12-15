from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404
from choice.models import Choice
from vote.models import Vote


def votes(request: HttpRequest) -> HttpResponse:
    choice = get_object_or_404(Choice, id=request.POST.get("choice_id", None))
    if choice == None:
        return redirect("poll:polls")
    poll = choice.poll
    Vote.objects.create(poll=poll, choice=choice)
    return redirect("poll:poll_results", poll_slug=poll.slug)
