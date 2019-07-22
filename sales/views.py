from .models import Customer, SoldProduct, SalesOrder, SalesOrderLine
from .serializers import (
    CustomerSerializer,
    SoldProductSerializer,
    SalesOrderSerializer,
    SalesOrderLineSerializer,
)
from rest_framework import viewsets


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class SoldProductViewSet(viewsets.ModelViewSet):
    queryset = SoldProduct.objects.all()
    serializer_class = SoldProductSerializer


class SalesOrderViewSet(viewsets.ModelViewSet):
    queryset = SalesOrder.objects.all()
    serializer_class = SalesOrderSerializer


class SalesOrderLineViewSet(viewsets.ModelViewSet):
    queryset = SalesOrderLine.objects.all()
    serializer_class = SalesOrderLineSerializer
