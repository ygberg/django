from django.shortcuts import render
from django.http import HttpResponse
from .models import Topic,Webpage,AccessRecords
from faker import Faker
# Create your views here.

def home_view(request,**kwargs):
    
    faker = Faker()

    new_topic = Topic(topic_name=faker.sentence(nb_words=2))
    new_webpage = Webpage(name=faker.sentence(nb_words=2), url=faker.url())
    new_accessRecords = AccessRecords(date=faker.date())
    
    my_dict =  {'insert_me':new_topic,'help_me':'www.google.se'}
    return render(request,"index.html",context = my_dict)

def help(request):
    return render(request,'project_two_templates\help.html',{})

