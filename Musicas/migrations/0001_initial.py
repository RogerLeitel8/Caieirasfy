# Generated by Django 2.2.5 on 2019-09-06 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Musica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomemsc', models.CharField(max_length=255, verbose_name='Nome da Musica')),
                ('nomeart', models.CharField(max_length=255, verbose_name='Nome do Artista')),
                ('gmsc', models.CharField(max_length=255, verbose_name='Gênero Musical')),
                ('link', models.CharField(max_length=255, verbose_name='Link da Musica')),
            ],
        ),
    ]
