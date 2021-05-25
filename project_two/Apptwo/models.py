from django.db import models
from faker import Faker

faker = Faker()
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

# for i in range(10):
#         new_topic = Topic(topic_name=faker.sentence(nb_words=2))
#         new_topic.save()

# for i in range(10):
#         new_webpage = Webpage(topic_id=i,name=faker.sentence(nb_words=2), url=faker.sentence(nb_words=2))
#         new_webpage.save()
# for i in range(10):
#         new_accessRecords = AccessRecords(date=faker.date())
#         new_accessRecords.save()