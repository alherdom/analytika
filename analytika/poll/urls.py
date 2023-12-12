from django.urls import path, include

from . import views

app_name = "poll"

urlpatterns = [
    path("", views.polls, name="polls"),
]
