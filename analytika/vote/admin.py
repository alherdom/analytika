from django.contrib import admin
from .models import Vote
from poll.models import Poll


@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ("id", "poll", "choice", "voted_at")
    list_filter = ("poll",)
