from django.db import models

# Create your models here.

class place(models.Model):
    cities = models.CharField(max_length=255)
    states = models.CharField(max_length=255)