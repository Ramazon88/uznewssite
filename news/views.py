from django.shortcuts import render, get_list_or_404
import requests as re
from django.core.paginator import Paginator

# Create your views here.
from news.models import *
yevro = re.get("https://nbu.uz/uz/exchange-rates/json/").json()[7]["cb_price"]
dollar = re.get("https://nbu.uz/uz/exchange-rates/json/").json()[23]["cb_price"]
rubl = re.get("https://nbu.uz/uz/exchange-rates/json/").json()[18]["cb_price"]
ctg = CategoryMode.objects.all()
actual = NewsMode.objects.filter(actual=True).order_by('-id')
actual1 = NewsMode.objects.filter(actual=True).order_by('-id')[4:8]
try:
    rek = Reklama.objects.filter(active=True).order_by('-id')[0]
except:
    rek = False

def homeViews(requests):
    main = NewsMode.objects.filter(main=True).order_by('-id')[0]
    news = NewsMode.objects.filter(main=False).order_by('-id')

    fliter_ctg_1 = NewsMode.objects.filter(ctg=1).order_by('-id')
    fliter_ctg_2 = NewsMode.objects.filter(ctg=2).order_by('-id')
    fliter_ctg_3 = NewsMode.objects.filter(ctg=4).order_by('-id')
    fliter_ctg_4 = NewsMode.objects.filter(ctg=5).order_by('-id')
    fliter_ctg_5 = NewsMode.objects.filter(ctg=6).order_by('-id')
    fliter_ctg_6 = NewsMode.objects.filter(ctg=3).order_by('-id')
    context = {'ctg': ctg, 'news': news, 'yevro': yevro, 'dollar': dollar, 'rubl': rubl,'main': main, 'actual': actual,
               'actual1': actual1,'moliya': fliter_ctg_1, 'jahon': fliter_ctg_2, 'talim': fliter_ctg_3, 'sport': fliter_ctg_4,
               'jamiyat': fliter_ctg_5, 'siyosat': fliter_ctg_6, 'rek': rek }
    return render(requests, 'index.html', context)



def ctgViews(requests, slug):
    ctg_one = CategoryMode.objects.get(ctg_slug=slug)
    reverse_news = NewsMode.objects.all().filter(ctg_id=ctg_one.id).order_by('-id')[1:]
    last_news = NewsMode.objects.all().filter(ctg_id=ctg_one.id).order_by('-id')[0]
    all_news = False
    paginator = Paginator(reverse_news, 5)
    page_number = requests.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'ctg': ctg, 'ctg_one': ctg_one, 'news': reverse_news, 'last': last_news, 'all_news': all_news, 'yevro': yevro,
               'dollar': dollar, 'rubl': rubl, 'actual': actual, 'actual1': actual1, 'page_obj': page_obj, 'rek': rek}
    return render(requests, 'category.html', context)


def allViews(requests):
    all_news = NewsMode.objects.all().order_by('-id')[1:]
    last_news = NewsMode.objects.all().order_by('-id')[0]
    paginator = Paginator(all_news, 5)
    page_number = requests.GET.get('page')
    page_obj = paginator.get_page(page_number)



    context = {'ctg': ctg, 'last_news': last_news, 'page_obj': page_obj, 'all_news': all_news, 'yevro': yevro,
               'dollar': dollar, 'rubl': rubl, 'actual': actual, 'actual1': actual1, 'rek': rek}
    return render(requests, 'category.html', context)


def newsViews(requests, pk):
    newsall = NewsMode.objects.all().order_by('-id')
    news = NewsMode.objects.get(id=pk)
    a, b = news.text.split("</p>", maxsplit=1)

    context = {'ctg': ctg, 'news': news, 'a': a, 'b': b, 'newsall': newsall, 'yevro': yevro, 'dollar': dollar,
               'rubl': rubl, 'actual1': actual1, 'actual': actual, 'rek': rek}
    return render(requests, 'view.html', context)


def searchViews(requests):
    soz = requests.GET.get('q', '')
    if soz and soz != '' and len(soz) >= 3:
        result = NewsMode.objects.filter(title__contains=soz).all()
    else:
        result = []
    lenght = len(result)
    context = {'ctg': ctg, 'page_obj': result, 'len': lenght, 'soz': soz, 'yevro': yevro, 'dollar': dollar,
               'rubl': rubl, 'actual': actual, 'actual1': actual1, 'rek': rek}
    return render(requests, 'search.html', context)


def contactViews(requests):
    root = Contact()
    if requests.POST:
        root.first_name = requests.POST.get('first_name')
        root.phone_number = requests.POST.get('phone_number')
        root.email = requests.POST.get('email')
        root.text = requests.POST.get('text')
        root.save()
        saved = requests.POST.get('first_name')
    else:
        saved = False
    context = {'ctg': ctg, 'saved': saved, 'yevro': yevro, 'dollar': dollar,
               'rubl': rubl, 'rek': rek}
    return render(requests, 'contact.html', context)

