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
        return f"{self.nick}"

class Miejsce(models.Model):
    latitude = models.DecimalField(
                max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(
                max_digits=9, decimal_places=6, null=True, blank=True)


class Zgloszenia(models.Model):
    zgloszenie_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(
        'Uzytkownik', models.DO_NOTHING, blank=True, null=True)
    sciezka_do_pliku = models.TextField()
    latitude = models.DecimalField(
                max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(
                max_digits=9, decimal_places=6, null=True, blank=True)
    data_czas = models.DateTimeField()
    akceptacja = models.IntegerField()
    opis = models.TextField()

    def __str__(self):
        return "Zgloszenie nr {}, Opis : {}".format(str(self.zgloszenie_id),str(self.opis))

    class Meta:
        managed = True
        db_table = 'Zgloszenia'


