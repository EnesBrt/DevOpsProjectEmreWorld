# Generated by Django 4.2.1 on 2023-05-23 18:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emre_world', '0007_alter_article_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='content',
        ),
    ]
