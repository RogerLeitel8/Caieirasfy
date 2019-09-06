from django.shortcuts import render
from rest_framework import viewsets
from Musicas.models import Musica
from Musicas.serializers import MusicaSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import SearchFilter


# Create your views here.
class MusicaViewSet(viewsets.ModelViewSet):
    queryset = Musica.objects.all()
    serializer_class = MusicaSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    authentication_classes = (TokenAuthentication,)
    filter_backends = [SearchFilter]
    search_fields = ['^nomemsc', '^nomeart', '^gmsc',]
