from .models import Drink
from .serializers import DrinkSerializer
from rest_framework import viewsets

class DrinkViewSet(viewsets.ModelViewSet):
    queryset = Drink.objects.all()
    serializer_class = DrinkSerializer