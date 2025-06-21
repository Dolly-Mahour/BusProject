from django.db import models

# Create your models here.

class Application_Users(models.Model):
    Username = models.CharField(max_length=255)
    User_or_Agent = models.BooleanField(default=True)
    Email = models.EmailField()
    Phone_number = models.IntegerField()
    Password = models.CharField(max_length=10)
    Referral_code = models.CharField(null=True,blank=True,max_length=255)

    def __str__(self):
        return self.Username