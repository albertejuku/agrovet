from django.shortcuts import render
from .models import Product
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

# Create your views here.
class ProductList(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'products/home.html'


class ProductCreate(CreateView):
    model = Product
    fields = [
        'name', 
        'description',
        'price',
        'stock',
        'category'
     ]
    template_name = 'products/create_product.html'


class ProductDetail(DetailView):
    model = Product
    template_name = 'products/product_detail.html'


class UpdateProduct(UpdateView):
    model = Product
    fields = [
        'name',
        'description',
        'price',
        'stock',
     ]
    template_name = 'products/update.html'
    success_url = ''


class Delete(DeleteView):
    model = Product
    template_name = 'products/delete.html'
    success_url = '../..'