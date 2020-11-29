# Generated by Django 3.1.2 on 2020-11-29 19:19

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RodzajZgloszenia',
            fields=[
                ('rodzaj_zgloszenia_id', models.AutoField(primary_key=True, serialize=False)),
                ('kategoria', models.TextField()),
                ('priorytet', models.IntegerField()),
            ],
            options={
                'db_table': 'RodzajZgloszenia',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Uzytkownik',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('nick', models.TextField()),
                ('imie', models.TextField()),
                ('nazwisko', models.TextField()),
                ('email', models.TextField()),
                ('organizacja', models.TextField()),
                ('uprawnienia', models.IntegerField()),
                ('liczba_zgloszen', models.IntegerField()),
                ('haslo', models.TextField()),
                ('latitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
            ],
            options={
                'db_table': 'Uzytkownik',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Zgloszenia',
            fields=[
                ('zgloszenie_id', models.AutoField(primary_key=True, serialize=False)),
                ('tytul_zgloszenia', models.TextField(null=True)),
                ('sciezka_do_pliku', models.TextField(blank=True, null=True)),
                ('latitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('data_czas', models.DateTimeField()),
                ('akceptacja', models.IntegerField()),
                ('opis', models.TextField()),
                ('rodzaj_zgloszenia', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='api.rodzajzgloszenia')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='api.uzytkownik')),
            ],
            options={
                'db_table': 'Zgloszenia',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='OcenyZgloszen',
            fields=[
                ('ocena_zgloszenia_id', models.AutoField(primary_key=True, serialize=False)),
                ('ocena', models.IntegerField(default=None, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)])),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.uzytkownik')),
                ('zgloszenie', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.zgloszenia')),
            ],
            options={
                'db_table': 'OcenyZgloszen',
                'managed': True,
            },
        ),
    ]
