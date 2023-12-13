from django.urls import path, include

from . import views

app_name = "choice"

urlpatterns = [
    path("", views.choices, name="choices"),
]
