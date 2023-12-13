from django.urls import path, include

from . import views

app_name = "poll"

urlpatterns = [
    path("", views.polls, name="polls"),
    path("poll/<slug:poll_slug>/vote", views.poll_vote, name="poll_vote"),
]
