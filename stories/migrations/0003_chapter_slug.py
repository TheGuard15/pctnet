# Generated by Django 2.1.3 on 2018-11-19 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0002_auto_20181119_0113'),
    ]

    operations = [
        migrations.AddField(
            model_name='chapter',
            name='slug',
            field=models.SlugField(default=''),
        ),
    ]
