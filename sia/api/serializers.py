from .models import *
from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_framework.serializers import Serializer, FileField


class UzytkownikSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Uzytkownik
        fields = '__all__'


class OcenyZgloszenSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OcenyZgloszen
        fields = '__all__'

class RodzajZgloszeniaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RodzajZgloszenia
        fields = '__all__'

class ZgloszeniaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Zgloszenia
        fields = '__all__'

class UploadSerializer(serializers.Serializer):
    file_uploaded = FileField()
    class Meta:
        fields = ['file_uploaded']
