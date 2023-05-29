from django.db import models
from tinymce import models as tinymce_models


class Article(models.Model):
    PAGE_CHOICES = (
        ('about', 'About'),
        ('reims', 'Reims'),
        ('metallurgie', 'Metallurgie'),
        ('entreprise', 'Entreprise'),
    )

    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    content = tinymce_models.HTMLField(blank=True, default="") # Utiliser le champ HTMLField de TinyMCE
    page = models.CharField(max_length=1000, choices=PAGE_CHOICES, default='about')

    def __str__(self):
        return self.title
