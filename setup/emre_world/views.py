from django.shortcuts import render
from .models import Article
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage
import os
from uuid import uuid4


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
def upload_image(request, series: str=None, article: str=None):
    if request.method != "POST":
        return JsonResponse({'Error Message': "Wrong request"})

    # If it's not series and not article, handle it differently
    matching_article = Article.objects.filter(series__slug=series, article_slug=article).first()
    if not matching_article:
        return JsonResponse({'Error Message': f"Wrong series ({series}) or article ({article})"})

    file_obj = request.FILES['file']
    file_name_suffix = file_obj.name.split(".")[-1]
    if file_name_suffix not in ["jpg", "png", "gif", "jpeg"]:
        return JsonResponse({"Error Message": f"Wrong file suffix ({file_name_suffix}), supported are .jpg, .png, .gif, .jpeg"})

    file_path = os.path.join(settings.MEDIA_ROOT, 'ArticleSeries', matching_article.slug, file_obj.name)

    if os.path.exists(file_path):
        file_obj.name = str(uuid4()) + '.' + file_name_suffix
        file_path = os.path.join(settings.MEDIA_ROOT, 'ArticleSeries', matching_article.slug, file_obj.name)

    with open(file_path, 'wb+') as f:
        for chunk in file_obj.chunks():
            f.write(chunk)

        return JsonResponse({
            'message': 'Image uploaded successfully',
            'location': os.path.join(settings.MEDIA_URL, 'ArticleSeries', matching_article.slug, file_obj.name)
        })