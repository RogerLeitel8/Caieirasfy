from django.db import models

# Create your models here.
class Musica(models.Model):
    nomemsc = models.CharField(
        max_length=255,
        verbose_name='Nome da Musica'
    )
    nomeart = models.CharField(
        max_length=255,
        verbose_name='Nome do Artista'
    )
    gmsc = models.CharField(
        max_length=255,
        verbose_name='Gênero Musical'
    )
    link = models.CharField(
        max_length=255,
        verbose_name='Link da Musica'
    )