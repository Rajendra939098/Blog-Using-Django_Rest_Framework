from django.db import models

# Create your models here.
class Task(models.Model):
    title=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    description=models.TextField(max_length=250)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    completed=models.BooleanField(default=True)
    image = models.ImageField(upload_to='task_images/', null=True, blank=True)
    url = models.URLField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.title
    



