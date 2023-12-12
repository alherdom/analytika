from django.contrib import admin
from .models import Choice


class ChoiceInline(admin.TabularInline):
    model = Choice


@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ("id", "poll", "name")
    list_editable = ("name",)
    inlines = [ChoiceInline]
