from rest_framework import permissions, viewsets, views, response
from django.contrib.auth import get_user_model

from .models import Pokemon
from .serializers import PokemonSerializer, UserSerializer
from .permissions import IsAdminOrReadOnly

# TODO: Consider changing to ReadOnlyModelViewSet
class PokemonViewSet(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer
    permission_classes = (IsAdminOrReadOnly,)

class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAdminUser,)

class GetAuthUser(views.APIView):
    permission_classes = (permissions.IsAuthenticated,)
    def get(self, request, format=None):
        return response.Response(
            UserSerializer(request.user, context={'request': request}).data
        )
