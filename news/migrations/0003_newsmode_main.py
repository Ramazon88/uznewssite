# Generated by Django 3.2.9 on 2021-12-10 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20211207_0928'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsmode',
            name='main',
            field=models.BooleanField(default=False),
        ),
    ]
