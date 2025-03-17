from django.db import models
# Create your models here.
class Musician(models.Model):
    first_name = models.CharField(max_length=20)
    last_Name = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length= 15,unique=True)
    INSTRUMENT_CHOICES = [
    ('Guitar', 'Guitar'),
    ('Piano', 'Piano'),
    ('Violin', 'Violin'),
    ('Drums', 'Drums'),
    ('Flute', 'Flute'),
    ]
    instrument = models.CharField(max_length=20,choices=INSTRUMENT_CHOICES)
    # instrument = models.CharField(max_length=20, choices=INSTRUMENT_CHOICES, default='Guitar')
    def __str__(self):
        return f"{self.first_name} {self.last_Name}-Instrument: {self.instrument}"
