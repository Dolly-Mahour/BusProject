from django.db import models

class Login_Users(models.Model):
    Phone_number = models.IntegerField()
    Password = models.CharField(max_length=8)

    def __str__(self):
        return self.Phone_number