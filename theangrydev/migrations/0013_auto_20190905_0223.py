# Generated by Django 2.2.5 on 2019-09-05 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theangrydev', '0012_auto_20190905_0158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(default='d04fdc4ddae6', max_length=100),
        ),
        migrations.AlterUniqueTogether(
            name='vote',
            unique_together={('user', 'post')},
        ),
    ]
