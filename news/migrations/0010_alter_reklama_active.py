# Generated by Django 3.2.9 on 2021-12-14 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0009_reklama_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reklama',
            name='active',
            field=models.BooleanField(default=False, verbose_name='Faolmi'),
        ),
    ]
