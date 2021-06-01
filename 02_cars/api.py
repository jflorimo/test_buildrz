from django.contrib.auth.models import User
from rest_framework import viewsets
from .models import Car


class CarViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Car to be viewed or edited.
    """

    queryset = Car.objects.all()
    serializer_class = Car
    permission_classes = []
