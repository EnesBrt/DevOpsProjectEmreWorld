from django.db import models

class Article(models.Model):
    PAGE_CHOICES = (
        ('about', 'About'),
        ('reims', 'Reims'),
        ('metallurgie', 'Metallurgie'),
        ('entreprise', 'Entreprise'),
    )

    title = models.CharField(max_length=200)
    slug = models.SlugField(default='default-slug', unique=True)
    content = models.TextField()
    page = models.CharField(max_length=200, choices=PAGE_CHOICES, default='about')

    def __str__(self):
        return self.title
