from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='TrackCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='Имя Категории')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
            ],
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True, verbose_name='Name')),
                ('streaming_link', models.CharField(blank=True, max_length=256, verbose_name='Stream')),
                ('link_to_aj', models.CharField(blank=True, max_length=256, verbose_name='aj_link')),
                ('download_link', models.FileField(upload_to='tracks/')),
                ('download_counter', models.PositiveIntegerField(default='0')),
                ('play_counter', models.PositiveIntegerField(default='0')),
                ('mood', models.CharField(blank=True, max_length=256, verbose_name='Mood')),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='mainapp.trackcategory')),
            ],
        ),
    ]
