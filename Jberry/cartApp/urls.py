from django.urls import path
from .import views
urlpatterns = [
    path('', views.cartshow, name='cartshow'),
    path('product/addto/', views.productaddtocart, name='productadd.to.cart'),
]
