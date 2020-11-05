from django.db import models


class OcenyZgloszen(models.Model):
    ocena_zgloszenia_id = models.AutoField(primary_key=True)
    zgloszenie = models.ForeignKey('Zgloszenia', models.DO_NOTHING)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    ocena = models.IntegerField()
    komentarz = models.TextField()

    class Meta:
        managed = False
        db_table = 'oceny_zgloszen'


class RodzajZgloszenia(models.Model):
    kategoria = models.TextField()
    waznosc = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'rodzaj_zgloszenia'


class Users(models.Model):
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
        managed = False
        db_table = 'users'


class Zgloszenia(models.Model):
    zgloszenie_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Users, models.DO_NOTHING)
    sciezka_do_pliku = models.TextField()
    wspolrzedne = models.TextField()
    data_czas = models.DateTimeField()
    akceptacja = models.IntegerField()
    opis = models.TextField()

    class Meta:
        managed = False
        db_table = 'zgloszenia'
