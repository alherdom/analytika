from django.contrib import admin
from .models import Choice


@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ("id", "poll", "name")
    list_editable = ("name",)
