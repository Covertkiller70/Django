from django.db import models

# Create your models here.
class Topic(models.Model):
    topname = models.CharField(max_length=255,unique=True)

    def __str__(self):
        return self.topname

class Webpage(models.Model):
    topic = models.ForeignKey(Topic, models.DO_NOTHING)
    name = models.CharField(max_length=255, unique=True)
    url = models.URLField(unique=True)
    
    def __str__(self):
        return self.name

class AccessRecord(models.Model):
    name = models.ForeignKey(Webpage,models.DO_NOTHING)
    date = models.DateField()

    def __str__(self):
        return str(self.date)
    