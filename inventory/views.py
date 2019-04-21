from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from .models import Product, Warehouse, Location


class ProductList(ListView):
    model = Product
    paginate_by = 10


class ProductCreate(CreateView):
    model = Product
    fields = ["name"]


class ProductDetail(DetailView):
    model = Product


class WarehouseCreate(CreateView):
    model = Warehouse
    fields = ["name"]


class WarehouseList(ListView):
    model = Warehouse
    paginate_by = 10


class WarehouseDetail(DetailView):
    model = Warehouse


class LocationList(ListView):
    model = Location
    paginate_by = 10


class LocationDetail(DetailView):
    model = Location
