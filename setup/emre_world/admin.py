from django.contrib import admin
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'content', 'page')  # Ajoutez image ici si vous avez un champ image dans votre modèle
    search_fields = ['title']

admin.site.register(Article, ArticleAdmin)
