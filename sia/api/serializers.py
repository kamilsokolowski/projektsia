from .models import *
from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_framework.serializers import Serializer, FileField


class UzytkownikSerializer(serializers.ModelSerializer):
    class Meta:
        model = Uzytkownik
        fields = '__all__'


class OcenyZgloszenSerializer(serializers.ModelSerializer):
    class Meta:
        model = OcenyZgloszen
        fields = '__all__'

class RodzajZgloszeniaSerializer(serializers.ModelSerializer):
    class Meta:
        model = RodzajZgloszenia
        fields = '__all__'

class ZgloszeniaSerializer(serializers.ModelSerializer):
    nick = serializers.SerializerMethodField('get_nick_name')
    rodzaj = serializers.SerializerMethodField('get_rodzaj_zgloszenia')

    class Meta:
        model = Zgloszenia
        fields = [
            'zgloszenie_id', 
            'user', 
            'nick',
            'rodzaj_zgloszenia',
            'rodzaj',
            'sciezka_do_pliku',
            'latitude',
            'longitude',
            'data_czas',
            'akceptacja',
            'opis'
        ]
    
    def get_nick_name(self, obj):
        return str(obj.user)

    def get_rodzaj_zgloszenia(self, obj):
        return str(obj.rodzaj_zgloszenia)

class UploadSerializer(serializers.Serializer):
    file_uploaded = FileField()
    class Meta:
        fields = ['file_uploaded']
