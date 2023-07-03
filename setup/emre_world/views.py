from django.shortcuts import render
from .models import Article
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage

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

@csrf_exempt
def upload_image(request):
    file = request.FILES['file']
    file_name = default_storage.save(file.name, file)
    return JsonResponse({'location': default_storage.url(file_name)})
