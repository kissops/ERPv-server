from .models import Warehouse, Product, Location, LocationQuantity
from .serializers import (
    WarehouseSerializer,
    ProductSerializer,
    LocationSerializer,
    LocationQuantitySerializer,
)
from rest_framework import viewsets


class WarehouseViewSet(viewsets.ModelViewSet):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class LocationQuantityViewSet(viewsets.ModelViewSet):
    queryset = LocationQuantity.objects.all()
    serializer_class = LocationQuantitySerializer
