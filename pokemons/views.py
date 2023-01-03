from rest_framework import permissions, viewsets
from django.contrib.auth import get_user_model

from .models import Pokemon
from .serializers import PokemonSerializer, UserSerializer
from .permissions import IsAdminOrReadOnly

# Create your views here.
class PokemonViewSet(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer
    permission_classes = (IsAdminOrReadOnly,)

# TODO: Change the permission
class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)
