from .models import Customer, CustomerContact, SoldProduct, SalesOrder, SalesOrderLine
from .serializers import (
    CustomerSerializer,
    CustomerContactSerializer,
    SoldProductSerializer,
    SalesOrderSerializer,
    SalesOrderLineSerializer,
)
from rest_framework import viewsets


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerContactViewSet(viewsets.ModelViewSet):
    queryset = CustomerContact.objects.all()
    serializer_class = CustomerContactSerializer


class SoldProductViewSet(viewsets.ModelViewSet):
    queryset = SoldProduct.objects.all()
    serializer_class = SoldProductSerializer


class SalesOrderViewSet(viewsets.ModelViewSet):
    queryset = SalesOrder.objects.all()
    serializer_class = SalesOrderSerializer


class SalesOrderLineViewSet(viewsets.ModelViewSet):
    queryset = SalesOrderLine.objects.all()
    serializer_class = SalesOrderLineSerializer
