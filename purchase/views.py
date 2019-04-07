from django.views.generic import ListView, DetailView
from .models import PurchaseOrder


class DeliverySchedule(ListView):
    model = PurchaseOrder
    paginate_by = 10
    template_name = "purchase/delivery_schedule.html"


class DeliveryDetail(DetailView):
    model = PurchaseOrder
    template_name = "purchase/delivery_detail.html"
