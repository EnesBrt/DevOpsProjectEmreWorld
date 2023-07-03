from django.db import migrations
import filebrowser.fields


class Migration(migrations.Migration):

    dependencies = [
        ('emre_world', '0010_alter_article_page'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image',
            field=filebrowser.fields.FileBrowseField(blank=True, max_length=200, null=True, verbose_name='Image'),
        ),
    ]