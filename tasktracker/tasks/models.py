from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    due_date = models.DateTimeField()
    progress = models.CharField(
    max_length=20, 
    choices=[('in_progress', 'In Progress'), ('completed', 'Completed')], 
    default='in_progress'  # Add default value
)
    def __str__(self):
        return self.title  # Corrected typo
