from django.db import models
from poll.models import Poll


class Choice(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.poll} {self.choice_text} {self.votes}"