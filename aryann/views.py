from django.shortcuts import render
from store.models import Product, ReviewRating
from django.http import HttpResponse

def home(request):
    products = Product.objects.all().filter(is_featured=True).order_by('-id')[:8]

    # Get the reviews
    reviews = None
    for product in products:
        reviews = ReviewRating.objects.filter(product_id=product.id, status=True)

    context = {
        'products': products,
        'reviews': reviews,
    }
    return render(request, 'home.html', context)

def contactus(request):
    return render(request, 'accounts/contactus.html')

def sitemap(request):
     return HttpResponse(open('sitemap.xml').read(), content_type='text/xml')
