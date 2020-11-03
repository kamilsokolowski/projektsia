from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.response import Response

from .views import UploadViewSet

class TestUploadViewSet(TestCase):
    def test_list(self):

        self.assertEqual(
            UploadViewSet.list(self,TestUploadViewSet).data,
            Response('GET API').data
        )


