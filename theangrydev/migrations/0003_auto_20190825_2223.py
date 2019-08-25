# Generated by Django 2.2.4 on 2019-08-25 22:23

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theangrydev', '0002_content_contenttype'),
    ]

    operations = [
        migrations.AddField(
            model_name='contenttype',
            name='metadata',
            field=django.contrib.postgres.fields.jsonb.JSONField(null=True),
        ),
        migrations.AlterField(
            model_name='content',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='content',
            name='text',
            field=models.TextField(blank=True, null=True),
        ),
    ]
