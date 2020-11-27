from .models import *

from django.contrib import admin
from django.conf import settings


admin.site.register(OcenyZgloszen)
admin.site.register(RodzajZgloszenia)
admin.site.register(Uzytkownik)

class ZgloszenieAdmin(admin.ModelAdmin):
    list_display = ('user', 'sciezka_do_pliku','opis', 'latitude', 'longitude',)

    fieldsets = (
        (None, {
            'fields': ('user', 'data_czas', 'sciezka_do_pliku', 'opis','latitude', 'akceptacja', 'longitude',)
        }),
    )

    class Media:
        if hasattr(settings, 'GOOGLE_MAPS_API_KEY') and settings.GOOGLE_MAPS_API_KEY:
            css = {
                'all': ('css/admin/location_picker.css',),
            }
            js = (
                'https://maps.googleapis.com/maps/api/js?key={}'.format(settings.GOOGLE_MAPS_API_KEY),
                'js/admin/location_picker.js',
            )

admin.site.register(Zgloszenia,ZgloszenieAdmin)


class MiejsceAdmin(admin.ModelAdmin):
    list_display = ('latitude', 'longitude',)

    fieldsets = (
        (None, {
            'fields': ( 'latitude', 'longitude',)
        }),
    )

    class Media:
        if hasattr(settings, 'GOOGLE_MAPS_API_KEY') and settings.GOOGLE_MAPS_API_KEY:
            css = {
                'all': ('css/admin/location_picker.css',),
            }
            js = (
                'https://maps.googleapis.com/maps/api/js?key={}'.format(settings.GOOGLE_MAPS_API_KEY),
                'js/admin/location_picker.js',
            )


admin.site.register(Miejsce, MiejsceAdmin)
