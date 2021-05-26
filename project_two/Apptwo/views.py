from django.shortcuts import render
from django.http import HttpResponse
from .models import Topic,Webpage,AccessRecords

# Create your views here.

def home_view(request,**kwargs):
    
    my_dict =  {'insert_me':new_topic,'help_me':'www.google.se'}
    return render(request,"index.html",context = my_dict)

def help(request):
    return render(request,'project_two_templates\help.html',{})

