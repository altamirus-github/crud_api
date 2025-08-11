from django.contrib import admin
from genres.models import Genre


@admin.register(Genre)
class ActorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
