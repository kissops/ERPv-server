from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from .models import Supplier, PurchaseOrder


class SupplierCreate(CreateView):
    model = Supplier
    fields = ["name", "address", "postcode"]


class SupplierList(ListView):
    model = Supplier
    paginate_by = 10


class SupplierDetail(DetailView):
    model = Supplier


class DeliverySchedule(ListView):
    model = PurchaseOrder
    paginate_by = 10
    template_name = "purchase/delivery_schedule.html"
    queryset = PurchaseOrder.objects.filter(complete=False)


class DeliveryDetail(DetailView):
    model = PurchaseOrder
    template_name = "purchase/delivery_detail.html"
    queryset = PurchaseOrder.objects.filter(complete=False)
