from django.views.generic import ListView, DetailView
from .models import SalesOrder


class ShipmentSchedule(ListView):
    model = SalesOrder
    paginate_by = 10
    template_name = "sales/shipment_schedule.html"
    queryset = SalesOrder.objects.filter(complete=False)


class ShipmentDetail(DetailView):
    model = SalesOrder
    template_name = "sales/shipment_detail.html"
    queryset = SalesOrder.objects.filter(complete=False)
