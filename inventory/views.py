from django.views.generic import ListView, DetailView
from .models import Product


class ProductList(ListView):
    model = Product
    paginate_by = 10
