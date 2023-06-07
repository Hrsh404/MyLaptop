from django.shortcuts import render
from . models import Client
# Create your views here.

def home(request):  
    clients= Client.objects.all()
    data= {
        'clients': clients   ,
    }
    return render (request, "pages/home.html", data)
def about(request): 
    return render (request, "pages/about.html")
def services(request): 
    return render (request, "pages/services.html")

def contact(request): 
    return render (request, "pages/contact.html")

