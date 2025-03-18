from django.db import models
from tasks.models import Task_Model
# Create your models here.

class Category_Model(models.Model):
    Category_Name = models.CharField(max_length=255,unique=True)
    task_model = models.ManyToManyField(Task_Model,related_name='category',blank=True)

    def __str__(self):
        return self.Category_Name