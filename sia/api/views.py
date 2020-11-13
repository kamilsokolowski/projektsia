from .serializers import *
from .models import *

from django.contrib.auth.models import User, Group
from django.core.files.storage import FileSystemStorage
from rest_framework import viewsets
from rest_framework.response import Response


class UzytkownikViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Uzytkownik.objects.all()
    serializer_class = UzytkownikSerializer


class OcenyZgloszenViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = OcenyZgloszen.objects.all()
    serializer_class = OcenyZgloszenSerializer

class RodzajZgloszeniaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = RodzajZgloszenia.objects.all()
    serializer_class = RodzajZgloszeniaSerializer

class ZgloszeniaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Zgloszenia.objects.all()
    serializer_class = ZgloszeniaSerializer


class UploadViewSet(viewsets.ViewSet):
    serializer_class = UploadSerializer

    def list(self, request):
        return Response("GET API")

    def create(self, request):
        file_uploaded = request.FILES.get('file_uploaded')
        content_type = file_uploaded.content_type
        fs = FileSystemStorage(location = 'media/files/')
        file = fs.save(file_uploaded.name, file_uploaded) 
        response = "POST API and you have uploaded a {} file".format(file_uploaded.name)
        return Response(response)

