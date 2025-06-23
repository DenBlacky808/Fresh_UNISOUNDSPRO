from django.db import models

class TrackCategory(models.Model):
    name = models.CharField(verbose_name='Имя Категории', max_length=64, unique=True)
    description = models.TextField(verbose_name='Описание', blank=True)

class Track(models.Model):
    name = models.CharField(verbose_name='Name', max_length=128, unique=True)
    streaming_link = models.CharField(verbose_name='Stream', max_length=256, blank=True)
    link_to_aj = models.CharField(verbose_name='aj_link', max_length=256, blank=True)
    download_link = models.FileField(upload_to='tracks/')
    download_counter = models.PositiveIntegerField(default='0')
    play_counter = models.PositiveIntegerField(default='0')
    category = models.ForeignKey(TrackCategory, on_delete=models.CASCADE, default=1)
    mood = models.CharField(verbose_name='Mood', max_length=256, blank=True)

# Create your models here.
