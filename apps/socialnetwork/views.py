from rest_framework import viewsets
from .models import SocialNetwork
from .serializer import SocialNetworkSerializer


class SocialNetworkViewSet(viewsets.ModelViewSet):
    queryset = SocialNetwork.objects.all()
    serializer_class = SocialNetworkSerializer
