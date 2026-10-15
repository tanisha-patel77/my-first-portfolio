from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'portfolio/index.html')

def contact_me(request):
    return render(request,'portfolio/contact_me.html')

def about_me(request):
    return render(request, 'portfolio/about_me.html')