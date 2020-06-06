# Generated by Django 3.0.6 on 2020-06-06 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theangrydev', '0024_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
