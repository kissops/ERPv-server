from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from .models import Supplier, PurchaseOrder


class PurchaseOrderCreate(CreateView):
    model = PurchaseOrder
    fields = ["supplier"]

    def get_context_data(self, **kwargs):
        supplier = get_object_or_404(Supplier, pk=self.kwargs["pk"])
        kwargs["supplier"] = supplier
        return super().get_context_data(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        self.pk = get_object_or_404(Supplier, pk=kwargs["pk"])
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.pk = self.pk
        return super().form_valid(form)


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
