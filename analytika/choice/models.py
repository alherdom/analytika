from django.db import models
from poll.models import Poll


class Choice(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name="choices")
    name = models.CharField(max_length=200)

    def get_percentage(self) -> float:
        votes = self.votes.count()
        total_votes = self.poll.votes.count()
        return round(votes / total_votes * 100, 2)

    def __str__(self):
        return f"{self.poll} {self.name}"
