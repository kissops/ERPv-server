from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from .models import Customer, SalesOrder


class CustomerCreate(CreateView):
    model = Customer


class CustomerList(ListView):
    model = Customer
    paginate_by = 10


class CustomerDetail(DetailView):
    model = Customer


class ShipmentSchedule(ListView):
    model = SalesOrder
    paginate_by = 10
    template_name = "sales/shipment_schedule.html"
    queryset = SalesOrder.objects.filter(complete=False)


class ShipmentDetail(DetailView):
    model = SalesOrder
    template_name = "sales/shipment_detail.html"
    queryset = SalesOrder.objects.filter(complete=False)
