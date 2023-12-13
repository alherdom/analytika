from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404
from choice.models import Choice

def votes(request: HttpRequest) -> HttpResponse:
    choice = get_object_or_404(Choice, id=request.POST["choice_id"])
    poll = choice.poll
    return render(request, "votes.html")
