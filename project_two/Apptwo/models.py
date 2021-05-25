from django.db import models

# Create your models here.

class Topic(models.Model):
    topic_name = models.CharField(max_length= 2264, unique=True)
    
    def __str__(self) -> str:
        return self.topic_name

class Webpage(models.Model):
    topic = models.ForeignKey(Topic)
    name = models.CharField(max_length= 2264, unique=True)
    url = models.URLField(unique=True)
    def __str__(self) -> str:
        return self.name

class AccessRecords(models.Model):
    name = models.ForeignKey(Webpage)
    date = models.DateField()

    def __str__(self) -> str:
        return self.date
