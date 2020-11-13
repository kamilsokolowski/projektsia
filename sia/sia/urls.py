from django.contrib import admin
from django.urls import include, path, re_path
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'uzytkownik', views.UzytkownikViewSet)
router.register(r'ocen-zgloszenia', views.OcenyZgloszenViewSet)
router.register(r'rodzaj-zgloszenia', views.RodzajZgloszeniaViewSet)
router.register(r'zgloszenia', views.ZgloszeniaViewSet)
router.register(r'upload', views.UploadViewSet, basename="upload")
# Setup automatic URL routing
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
