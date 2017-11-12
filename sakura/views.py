from django.shortcuts import render
from django.http import HttpResponse

def index(request):
   return HttpResponse("This is not the season for sakura.")
# Create your views here.

