from django.db import models

from django.urls import reverse


class Poll(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    active = models.BooleanField(default=True)
    opened_from = models.DateTimeField()
    opened_to = models.DateTimeField()

    class Meta:
        ordering = ("-opened_from",)
        indexes = [models.Index(fields=["name"])]

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self) -> str:
        return reverse("poll:poll_vote", kwargs=dict(poll_slug=self.slug))
