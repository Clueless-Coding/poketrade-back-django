from rest_framework import viewsets

from .models import Pokemon
from .serializers import PokemonSerializer

# Create your views here.
class PokemonViewSet(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer