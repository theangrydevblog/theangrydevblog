# Generated by Django 2.2.4 on 2019-09-02 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theangrydev', '0007_auto_20190831_1059'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('admin', models.BooleanField(default=False)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
