from django.contrib import admin

from .models import Track, TrackCategory


@admin.register(TrackCategory)
class TrackCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'category',
        'download_counter',
        'play_counter',
    )
