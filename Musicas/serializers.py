from rest_framework import serializers
from Musicas.models import Musica


class MusicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Musica
        fields = ('nomemsc', 'nomeart', 'gmsc', 'link')
        fields = '__all__'
