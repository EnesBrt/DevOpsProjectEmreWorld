from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def home(request):
    return render(request, 'emre_world/home.html')

def about(request):
    return render(request, 'emre_world/about.html')

def reims(request):
    return render(request, 'emre_world/reims.html')

def metallurgie(request):
    return render(request, 'emre_world/metallurgie.html')

def entreprise(request):
    return render(request, 'emre_world/entreprise.html')
