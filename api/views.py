from rest_framework import generics
from django.shortcuts import render

# get list
from api.serializer import *
from news.models import *


class NewsListView(generics.ListAPIView):
    queryset = NewsMode.objects.filter(telegram_bot=True)
    serializer_class = NewsSerializers


class NewsUpdView(generics.UpdateAPIView):
    queryset = NewsMode.objects.all()
    serializer_class = NewsUpdSerializers


class ContactListView(generics.ListAPIView):
    queryset = Contact.objects.filter(active=True)
    serializer_class = ContactSerializers


class ContactUpdView(generics.UpdateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactUpdSerializers
