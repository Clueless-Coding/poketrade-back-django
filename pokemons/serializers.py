from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import Pokemon

class PokemonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pokemon
        fields = ('url', 'id', 'name', 'worth', 'height', 'weight', 'image', 'types')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('url', 'id', 'username', 'pokemons')
