from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home_view(request,**kwargs):
    my_dict =  {'insert_me':'this is from views!','help':'/help'}
    return render(request,"index.html",context = my_dict)

def help(request):
    return render(request,'project_two_templates\help.html',{})