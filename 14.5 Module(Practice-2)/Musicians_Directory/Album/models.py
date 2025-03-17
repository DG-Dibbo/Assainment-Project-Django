from django.db import models
from django.utils import timezone
class Album(models.Model):
    album_name = models.CharField(max_length=100,unique=True)
    release_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.album_name} Release Date: {self.release_date.strftime('%Y-%m-%d %I:%M:%S %p')}"
