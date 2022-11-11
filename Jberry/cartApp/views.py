from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required

# This is functional part ....


def cartshow(request):
    return render(request, 'cart.html')

# Only For authenticate logged user ....


@login_required
def productaddtocart(request):
    # category_id = request.POST['']
    product_id = request.POST['product_id']
    quantity = request.POST['quantity']
    print(product_id, quantity)
    return HttpResponse([product_id, quantity])

# This Login section End Here ....
