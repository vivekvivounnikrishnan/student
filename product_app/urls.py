from django.urls import path
from product_app.views import *

urlpatterns = [
    path('category/list',Category_list,name='Category-list'),
    path('product/list',Product_list,name='Product-list'),
    path('size/list',Size_list,name='Size-list'),
    path('size/<int:size_id>/list',Size_list_one,name='Size-list')
]
