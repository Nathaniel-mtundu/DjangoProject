#from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    #return HttpResponse('hi, welcome to my home page')
    return render(request, 'home.html')
def about(request):
    #return HttpResponse("hi bro, welcome to my about page")
    return render(request, 'about.html')
