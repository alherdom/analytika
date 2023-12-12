from django.contrib import admin
from .models import Poll


@admin.register(Poll)
class PollAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "slug", "active", "opened_from", "opened_to")
    list_editable = ("name", "slug", "active", "opened_from", "opened_to")
    prepopulated_fields = dict(slug=("name",))
