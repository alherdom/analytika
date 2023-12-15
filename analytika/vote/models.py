from django.db import models
from poll.models import Poll
from choice.models import Choice
from django.urls import reverse


class Vote(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name="votes")
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE, related_name="votes")
    voted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.poll} {self.choice} {self.voted_at}"