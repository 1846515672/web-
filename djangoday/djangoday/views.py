from django.shortcuts import render
from django.shortcuts import render_to_response
from appName.models import *
# Create your views here.

def about_us(request):
    listnews = News.objects.all()
    return render_to_response('about-us.html',locals())

def index(request):
    return render_to_response('index.html',locals())