from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('reims/', views.reims, name='reims'),
    path('metallurgie/', views.metallurgie, name='metallurgie'),
    path('entreprise/', views.entreprise, name='entreprise'),
]
