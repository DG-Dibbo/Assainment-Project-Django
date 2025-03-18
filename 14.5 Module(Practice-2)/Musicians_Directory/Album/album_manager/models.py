from django.db import models
from django.utils import timezone
from musician.models import Musician
class Album_View(models.Model):
    name = models.CharField(max_length=20,unique=True)
    email = models.EmailField(unique=True)
    album_name = models.CharField(max_length=100)
    instrument = models.ManyToManyField(Musician)
    release_date = models.DateTimeField(auto_now_add=True)
    Choice_Rating = [
       ('1','1'),
       ('2','2'),
       ('3','3'),
       ('4','4'),
       ('5','5'),
    ]
    Rating = models.CharField(max_length=20,choices=Choice_Rating)
    def __str__(self):
        return f"{self.album_name} Release Date: {self.release_date.strftime('%Y-%m-%d %I:%M:%S %p')}"
