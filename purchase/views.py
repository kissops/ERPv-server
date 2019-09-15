from .models import (
    Supplier,
    SupplierContact,
    PurchasedProduct,
    PurchaseOrder,
    PurchaseOrderLine,
)
from .serializers import (
    SupplierSerializer,
    SupplierContactSerializer,
    PurchasedProductSerializer,
    PurchaseOrderSerializer,
    PurchaseOrderLineSerializer,
)
from rest_framework import viewsets


class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer


class SupplierContactViewSet(viewsets.ModelViewSet):
    queryset = SupplierContact.objects.all()
    serializer_class = SupplierContactSerializer


class PurchasedProductViewSet(viewsets.ModelViewSet):
    queryset = PurchasedProduct.objects.all()
    serializer_class = PurchasedProductSerializer


class PurchaseOrderViewSet(viewsets.ModelViewSet):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer


class PurchaseOrderLineViewSet(viewsets.ModelViewSet):
    queryset = PurchaseOrderLine.objects.all()
    serializer_class = PurchaseOrderLineSerializer
