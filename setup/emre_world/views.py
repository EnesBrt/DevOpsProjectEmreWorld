from django.shortcuts import render
from .models import Article

def home(request):
    return render(request, 'emre_world/home.html')

def about(request):
    articles = Article.objects.filter(page='about')  # Récupérer tous les articles pour la page "About"
    return render(request, 'emre_world/about.html', {'articles': articles})

def reims(request):
    articles = Article.objects.filter(page='reims')  # Récupérer tous les articles pour la page "Reims"
    return render(request, 'emre_world/reims.html', {'articles': articles})

def metallurgie(request):
    articles = Article.objects.filter(page='metallurgie')  # Récupérer tous les articles pour la page "Metallurgie"
    return render(request, 'emre_world/metallurgie.html', {'articles': articles})

def entreprise(request):
    articles = Article.objects.filter(page='entreprise')  # Récupérer tous les articles pour la page "Entreprise"
    return render(request, 'emre_world/entreprise.html', {'articles': articles})
