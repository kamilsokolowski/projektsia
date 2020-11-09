# Generated by Django 3.1.2 on 2020-11-05 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OcenyZgloszen',
            fields=[
                ('ocena_zgloszenia_id', models.AutoField(primary_key=True, serialize=False)),
                ('ocena', models.IntegerField()),
                ('komentarz', models.TextField()),
            ],
            options={
                'db_table': 'oceny_zgloszen',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='RodzajZgloszenia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kategoria', models.TextField()),
                ('waznosc', models.IntegerField()),
            ],
            options={
                'db_table': 'rodzaj_zgloszenia',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('nick', models.TextField()),
                ('imie', models.TextField()),
                ('nazwisko', models.TextField()),
                ('organizacja', models.TextField()),
                ('uprawnienia', models.IntegerField()),
                ('liczba_zgloszen', models.IntegerField()),
                ('haslo', models.TextField()),
                ('awatar', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'users',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Zgloszenia',
            fields=[
                ('zgloszenie_id', models.AutoField(primary_key=True, serialize=False)),
                ('sciezka_do_pliku', models.TextField()),
                ('wspolrzedne', models.TextField()),
                ('data_czas', models.DateTimeField()),
                ('akceptacja', models.IntegerField()),
                ('opis', models.TextField()),
            ],
            options={
                'db_table': 'zgloszenia',
                'managed': False,
            },
        ),
    ]