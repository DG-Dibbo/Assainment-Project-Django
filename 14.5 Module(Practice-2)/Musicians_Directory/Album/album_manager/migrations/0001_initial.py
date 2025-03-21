# Generated by Django 5.1.7 on 2025-03-16 22:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AlbumSet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album_name', models.CharField(max_length=100, unique=True)),
                ('release_date', models.DateTimeField(auto_now_add=True)),
                ('album_set', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='album_manager.albumset')),
            ],
        ),
    ]
