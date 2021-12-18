from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.
class CategoryMode(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nomi')
    ctg_slug = models.CharField(max_length=50, verbose_name='Kategoriya slugi')
    active = models.BooleanField(default=True, verbose_name='Faolligi')

    def __str__(self):
        return self.name


class NewsMode(models.Model):
    title = models.CharField(max_length=200, verbose_name='Sarlavha')
    text = RichTextField(verbose_name='Matn')
    time = models.DateTimeField(auto_now_add=True)
    ctg = models.ForeignKey(CategoryMode, on_delete=models.CASCADE, verbose_name='Kategoriya')
    image_1 = models.ImageField(null=False, verbose_name='Birinchi rasm')
    image_2 = models.ImageField(null=True, blank=True, verbose_name='Ikkinchi rasm')
    image_3 = models.ImageField(null=True, blank=True, verbose_name='Uchnchi rasm')
    author = models.CharField(max_length=200, verbose_name='Yozuvchi ismi')
    main = models.BooleanField(default=False, verbose_name='Asosiymi')
    actual = models.BooleanField(default=False, verbose_name='Dolzarbmi')
    telegram_bot = models.BooleanField(default=False, verbose_name='Telegramga kanalga yuborilsinmi')

    def __str__(self):
        return self.title


class Reklama(models.Model):
    text = models.CharField(max_length=200, verbose_name='Nomi')
    url = models.URLField(verbose_name='Veb-manzili')
    image = models.ImageField(null=False, verbose_name='Rasmi')
    time = models.DateTimeField(auto_now_add=True, verbose_name='Qo`yilgan vaqt')
    active = models.BooleanField(default=False, verbose_name='Faolmi')

    def __str__(self):
        return self.text


class Contact(models.Model):
    first_name = models.CharField(max_length=200, verbose_name='Ismi')
    phone_number = models.CharField(max_length=200, verbose_name='Telefon raqami')
    email = models.EmailField(verbose_name='Elektron pochtasi')
    text = models.TextField(null=True, blank=True, verbose_name='Xabar')
    time = models.DateTimeField(auto_now_add=True, verbose_name='Vaqti')
    active = models.BooleanField(default=True, verbose_name='Faolmi')

    def __str__(self):
        return self.first_name
