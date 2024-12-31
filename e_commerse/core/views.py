from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'core/index.html')

def product_details(request):
    return render(request, 'core/contentDetails.html')