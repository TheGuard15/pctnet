# Generated by Django 2.1.3 on 2018-11-19 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0005_auto_20181119_0451'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='isdeleted',
            field=models.BooleanField(default=False),
        ),
    ]
