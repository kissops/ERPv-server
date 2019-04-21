from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from .models import Customer, SalesOrder


class SalesOrderCreate(CreateView):
    model = SalesOrder
    fields = ["customer"]

    def get_context_data(self, **kwargs):
        customer = get_object_or_404(Customer, pk=self.kwargs["pk"])
        kwargs["customer"] = customer
        return super().get_context_data(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        self.pk = get_object_or_404(Customer, pk=kwargs["pk"])
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.pk = self.pk
        return super().form_valid(form)


class CustomerCreate(CreateView):
    model = Customer
    fields = ["name", "address", "postcode", "phone", "email", "website"]


class CustomerUpdate(UpdateView):
    model = Customer
    fields = ["name", "address", "postcode", "phone", "email", "website"]


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
