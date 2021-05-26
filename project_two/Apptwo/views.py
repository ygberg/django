from django.shortcuts import render
from django.http import HttpResponse
from .models import Topic,Webpage,AccessRecords
from itertools import chain

# Create your views here.

def home_view(request,**kwargs):
    
    topics = Topic.objects.all()
    webpage = Webpage.objects.all()
    access = AccessRecords.objects.all()
    context = {'topics': topics,'webpage':webpage,'access':access}

    web = Webpage.objects.values_list('name')
    acc = AccessRecords.objects.values_list('name')
    webrecords = web.union(acc).order_by('name')
    
    return render(request,"index.html",{'topics': topics,'webpage':webpage,'access':access,'webrecords':webrecords,'web':web,'acc':acc})

def help(request):
    return render(request,'project_two_templates\help.html',{})

