from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_framework.serializers import Serializer, FileField


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class UploadSerializer(serializers.Serializer):
    file_uploaded = FileField()
    class Meta:
        fields = ['file_uploaded']
