#from project_two.Apptwo.models import Topic,Webpage,AccessRecords
from django.core.management.base import BaseCommand
from faker import Faker
from Apptwo.models import Topic,Webpage,AccessRecords
# from models import Topic,Webpage,AccessRecords
# Create your tests here.


class Command(BaseCommand):
        help = 'Command information '

        def handle(self, *args, **kwargs):
                
                fake = Faker()
                
                for _ in range(10):
                        topi = fake.unique.sentence(nb_words=2)
                        top =Topic.objects.get_or_create(topic_name =topi)[0]

                
                        
                        #topic_name_fromtopic = Topic.objects.get(pk=i)
                        ur = fake.unique.domain_name()
                        nam = fake.unique.sentence(nb_words=2)
                        webpg = Webpage.objects.get_or_create(topic = top, name=nam,url=ur)[0]

                
                        #wepage_name = Webpage.objects.filter(name__pk=i)
                        dt = fake.date()
                        AccessRecords.objects.create(name =webpg, date=dt)

                #print(Webpage.objects.all())
                
            


# faker = Faker()

# new_topic = Topic(topic_name=faker.sentence(nb_words=2))
# new_webpage = Webpage(name=faker.sentence(nb_words=2), url=faker.url())
# new_accessRecords = AccessRecords(date=faker.date())



# class TestData(Topic,Webpage,AccessRecords):
   
    
#     def test_data(self):
#         self.faker = Faker()

#         new_topic = self.Topic(topic_name=self.fake.sentence(nb_words=2))
#         new_webpage = self.Webpage(name=self.fake.sentence(nb_words=2), url=self.faker.url())
#         new_accessRecords = self.AccessRecords(date=self.faker.date())

        # new_topic = self.Topic(topic_name='first order')
        # new_webpage = self.Webpage(Topic__id=1, name='order here', url='www.order.com')
        # new_accessRecords = self.AccessRecords(Webpage__id=1,date='2021-05-25')