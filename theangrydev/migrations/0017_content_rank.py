# Generated by Django 3.0.6 on 2020-05-11 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theangrydev', '0016_auto_20200506_0014'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='rank',
            field=models.IntegerField(default=0),
        ),
    ]
