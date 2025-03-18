from django.db import models

class Task_Model(models.Model):
    taskTitle = models.CharField(max_length=500)
    taskDescription = models.TextField()
    is_completed = models.BooleanField(default=False)
    task_assign_date = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField('categories.Category_Model', related_name='tasks')

    def __str__(self):
        return self.taskTitle
