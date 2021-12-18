from rest_framework import serializers

from news.models import *


class NewsSerializers(serializers.ModelSerializer):
    class Meta:
        model = NewsMode
        fields = '__all__'


class NewsUpdSerializers(serializers.ModelSerializer):
    class Meta:
        model = NewsMode
        fields = ('telegram_bot',)


class ContactSerializers(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


class ContactUpdSerializers(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('active',)
