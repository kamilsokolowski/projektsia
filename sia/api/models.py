from django.db import models


class OcenyZgloszen(models.Model):
    ocena_zgloszenia_id = models.AutoField(primary_key=True)
    zgloszenie = models.ForeignKey('Zgloszenia', models.DO_NOTHING)
    user = models.ForeignKey('Uzytkownik', models.DO_NOTHING)
    ocena = models.IntegerField()
    komentarz = models.TextField()

    class Meta:
        managed = True
        db_table = 'OcenyZgloszen'

    def __str__(self):
        return "Ocena o nr {} Ocena: {}".format(str(self.ocena_zgloszenia_id), str(self.ocena))


class RodzajZgloszenia(models.Model):
    kategoria = models.TextField()
    waznosc = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'RodzajZgloszenia'


class Uzytkownik(models.Model):
    user_id = models.AutoField(primary_key=True)
    nick = models.TextField()
    imie = models.TextField()
    nazwisko = models.TextField()
    organizacja = models.TextField()
    uprawnienia = models.IntegerField()
    liczba_zgloszen = models.IntegerField()
    haslo = models.TextField()
    awatar = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Uzytkownik'

    def __str__(self):
        return "Uzytkownik {} {} o nicku {} z user_id {}".format(str(self.imie), str(self.nazwisko), str(self.nick), str(self.user_id))


class Zgloszenia(models.Model):
    zgloszenie_id = models.AutoField(primary_key=True)
    user = models.ForeignKey('Uzytkownik', models.DO_NOTHING)
    sciezka_do_pliku = models.TextField()
    wspolrzedne = models.TextField()
    data_czas = models.DateTimeField()
    akceptacja = models.IntegerField()
    opis = models.TextField()

    def __str__(self):
        return "Zgloszenie nr {}, Opis : {}".format(str(self.zgloszenie_id),str(self.opis))

    class Meta:
        managed = True
        db_table = 'Zgloszenia'

from django.db import models


class Miejsce(models.Model):

    name = models.CharField(max_length=255)

    latitude = models.DecimalField(
                max_digits=9, decimal_places=6, null=True, blank=True)

    longitude = models.DecimalField(
                max_digits=9, decimal_places=6, null=True, blank=True)
