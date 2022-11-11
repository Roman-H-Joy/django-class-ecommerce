from django.urls import path
from .import views

urlpatterns = [
    path('', views.trendingproducts, name='trendingproducts'),
    path('filter/categoryway/show/<category>/',
         views.categoryWayProductShow, name='category.Way.Product.Show'),
    path('single/view/<str:name>/',
         views.productSingleView, name='product.single.view'),
    path('search', views.search, name="search"),
]
