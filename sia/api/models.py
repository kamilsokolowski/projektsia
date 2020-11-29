from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class OcenyZgloszen(models.Model):
    ocena_zgloszenia_id = models.AutoField(primary_key=True)
    zgloszenie          = models.ForeignKey('Zgloszenia', models.DO_NOTHING)
    user                = models.ForeignKey('Uzytkownik', models.DO_NOTHING)
    ocena               = models.IntegerField(
                            default=None,
                            validators=[MaxValueValidator(5), MinValueValidator(1)])

    class Meta:
        managed = True
        db_table = 'OcenyZgloszen'

    def __str__(self):
        return "Ocena o nr {} Ocena: {}".format(str(self.ocena_zgloszenia_id), str(self.ocena))


class RodzajZgloszenia(models.Model):
    rodzaj_zgloszenia_id = models.AutoField(primary_key=True)
    kategoria            = models.TextField()
    priorytet            = models.IntegerField()

    class Meta:
        managed  = True
        db_table = 'RodzajZgloszenia'
    
    def __str__(self):
        return f"{self.kategoria}"


class Uzytkownik(models.Model):
    user_id         = models.AutoField(primary_key=True)
    nick            = models.TextField()
    imie            = models.TextField()
    nazwisko        = models.TextField()
    email           = models.TextField()
    organizacja     = models.TextField()
    uprawnienia     = models.IntegerField()
    liczba_zgloszen = models.IntegerField()
    haslo           = models.TextField()

    class Meta:
        managed = True
        db_table = 'Uzytkownik'

    def __str__(self):
        return f"{self.nick}"


class Zgloszenia(models.Model):
    zgloszenie_id       = models.AutoField(primary_key=True)
    tytul_zgloszenia    = models.TextField(null=True)
    user                = models.ForeignKey(
                        'Uzytkownik', models.DO_NOTHING, blank=True, null=True)
    rodzaj_zgloszenia   = models.ForeignKey(
                        'RodzajZgloszenia', models.DO_NOTHING, blank=True, null=True)
    sciezka_do_pliku    = models.TextField(blank=True, null=True)
    latitude            = models.DecimalField(
                          max_digits=9, decimal_places=6, null=True, blank=True)
    longitude           = models.DecimalField(
                          max_digits=9, decimal_places=6, null=True, blank=True)
    data_czas           = models.DateTimeField()
    akceptacja          = models.IntegerField()
    opis                = models.TextField()

    def __str__(self):
        return "Zgloszenie nr {}, Opis : {}".format(str(self.zgloszenie_id),str(self.opis))

    class Meta:
        managed  = True
        db_table = 'Zgloszenia'


