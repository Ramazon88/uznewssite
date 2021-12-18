# Generated by Django 3.2.9 on 2021-12-14 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_newsmode_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('phone_number', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('text', models.TextField(blank=True, null=True)),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
