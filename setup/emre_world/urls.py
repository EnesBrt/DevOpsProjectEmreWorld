from django.urls import path
from . import views

app_name = 'emre_world'

urlpatterns = [
    path('upload_image/', views.upload_image, name='upload_image'),  # Nouvelle ligne ici.
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('reims/', views.reims, name='reims'),
    path('metallurgie/', views.metallurgie, name='metallurgie'),
    path('entreprise/', views.entreprise, name='entreprise'),
]
