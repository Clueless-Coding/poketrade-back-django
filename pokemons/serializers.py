from rest_framework import serializers

from .models import Pokemon

class PokemonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pokemon
        fields = ('url', 'id', 'name', 'worth', 'height', 'weight')