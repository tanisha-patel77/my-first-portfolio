from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'portfolio/index.html')

def contact(request):
    return render(request,'portfolio/contactme.html')

def aboutme(request):
    return render(request,'portfolio/aboutme.html')