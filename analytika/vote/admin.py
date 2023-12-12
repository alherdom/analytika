from django.contrib import admin
from .models import Vote


@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ("id", "poll", "choice", "voted_at")
    list_editable = ("poll", "choice", "voted_at")
