# Generated by Django 3.2.9 on 2021-12-10 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_newsmode_main'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsmode',
            name='actual',
            field=models.BooleanField(default=False),
        ),
    ]