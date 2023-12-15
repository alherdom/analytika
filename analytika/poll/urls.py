from django.urls import path, include

from . import views

app_name = "poll"

urlpatterns = [
    path("", views.polls, name="polls"),
    path("<slug:poll_slug>/", views.poll_choices, name="poll_choices"),
    path("<slug:poll_slug>/results/", views.poll_results, name="poll_results"),
]
