from django.shortcuts import render
from django.http import HttpResponse

from .models import Product

# Create your views here.
def home(request):
    products = Product.objects.all()
    context = {
        'product_list': products,
        'user': request.user
    }
    return render(request, 'store/home.html', context)
