from django.db import models

# Create your models here.
class User(models.Model):
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    def __str__(self):
        return self.email