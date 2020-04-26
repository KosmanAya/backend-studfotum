from django.db import models

# Create your models here.

class User(models.Model):
    name = models.TextField()
    email = models.TextField()
    status = models.TextField()
    avatar = models.TextField()

class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    title = models.TextField()
    text = models.TextField()
