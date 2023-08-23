from django.shortcuts import render

# Create your views here.

def index(request):
    context = {'title': 'Test Title',
               'username': 'Ssha',
               }

    return render(request, 'products/index.html')

def products(request):
    return render(request, 'products/products.html')