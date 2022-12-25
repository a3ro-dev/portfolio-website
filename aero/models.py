from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=80, blank=True)
    email = models.EmailField(max_length=100, blank=True)
    message = models.TextField(max_length=255, blank=True)
    date = models.DateTimeField()