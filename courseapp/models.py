from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Lesson(models.Model):
    LEVEL_CHOICES = [
        ('B', 'Beginner'),
        ('I', 'Intermediate'),
        ('A', 'Advanced'),
    ]

    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    points = models.IntegerField()
    level = models.CharField(max_length=1, choices=LEVEL_CHOICES)

    def __str__(self):
        return self.name
