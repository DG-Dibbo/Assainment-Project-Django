# Generated by Django 5.1.7 on 2025-03-17 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('album_manager', '0003_alter_album_view_album_name'),
        ('musician', '0003_alter_musician_email_alter_musician_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='album_view',
            name='instrument',
            field=models.ManyToManyField(to='musician.musician'),
        ),
    ]
