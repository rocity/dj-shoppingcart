from django.shortcuts import render
from django.http import HttpResponse

# decorators
from django.contrib.auth.decorators import login_required

from .models import Product

# Create your views here.
def home(request):
    products = Product.objects.all()
    context = {
        'product_list': products,
        'user': request.user
    }
    return render(request, 'store/home.html', context)

@login_required(login_url='/store/')
def profile(request):
    logged = None
    if request.user.is_authenticated():
        logged = request.user

    return render(request, 'store/profile.html', {'user': logged})
