from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from product.models import Product

from category.models import Category

# Create your views here.


def trendingproducts(request):
    products = Product.objects.all()
    categories = {product.category.name for product in products}
    # categories = Category.objects.all()
    # print(categories)
    contex = {
        'categories': categories,
        'products': products
    }
    return render(request, 'trending.html', contex)


def categoryWayProductShow(request, category):
    products = Product.objects.filter(category__name=category)
    categories = {category, }
    print(products)
    contex = {
        'categories': categories,
        'products': products
    }
    # return HttpResponse(products)
    return render(request, 'trending.html', contex)


def productSingleView(request, name):
    product = Product.objects.filter(name=name).first()
    # categories = {pro.category.name for pro in product}
    # categories = {product[0].category}
    # print(product)
    contex = {
        'product': product
    }
    return render(request, 'product-details.html', contex)


def search(request):
    search = request.POST['search'].split(' ')
    products = Product.objects.filter(
        name__icontains=search[0], description__icontains=search[0])
    for result in search[1:]:
        products = products.union(
            Product.objects.filter(
                name__icontains=result, description__icontains=result)
        )
    categories = {item.category for item in products}
    contex = {
        'categories': categories,
        'products': products
    }
    return render(request, 'trending.html', contex)
    # return HttpResponse(products)
