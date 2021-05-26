from django.shortcuts import render
from django.http import HttpResponse
from .models import Topic,Webpage,AccessRecords

# Create your views here.

def home_view(request,**kwargs):
    
    topics = Topic.objects.all()
    webpage = Webpage.objects.all()
    access = AccessRecords.objects.all()
    context = {'topics': topics,'webpage':webpage,'access':access}
    return render(request,"index.html",{'topics': topics,'webpage':webpage,'access':access})

def help(request):
    return render(request,'project_two_templates\help.html',{})

