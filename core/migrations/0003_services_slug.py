# Generated by Django 4.1.5 on 2023-02-13 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_blog_meta_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='slug',
            field=models.SlugField(blank=True, max_length=100, null=True, unique=True),
        ),
    ]