from django.db import models
# Create your models here.

class MyModel(models.Model):
    auto_field = models.AutoField(primary_key=True)
    # big_auto_field = models.BigAutoField(primary_key=True)
    big_integer_field = models.BigIntegerField(1000000000000000000)
    binary_field = models.BinaryField()
    boolean_field = models.BooleanField()
    char_field = models.CharField(max_length=255)
    date_field = models.DateField()
    date_time_field = models.DateTimeField()
    decimal_field = models.DecimalField(max_digits=5, decimal_places=2)
    duration_field = models.DurationField( )
    email_field = models.EmailField()
    float_field = models.FloatField()
    text_field = models.TextField()
    time_field = models.TimeField()

    def __str__(self):
        return self.char_field