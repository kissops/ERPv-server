from .models import BillOfMaterials, BOMItem, Job
from .serializers import BillOfMaterialsSerializer, BOMItemSerializer, JobSerializer
from rest_framework import viewsets


class BillOfMaterialsViewSet(viewsets.ModelViewSet):
    queryset = BillOfMaterials.objects.all()
    serializer_class = BillOfMaterialsSerializer


class BOMItemViewSet(viewsets.ModelViewSet):
    queryset = BOMItem.objects.all()
    serializer_class = BOMItemSerializer


class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
