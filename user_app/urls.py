from django.urls import path
from user_app.views import *

urlpatterns = [
    # path('login/', login_list, name='login-list'),
    # path('profileadd/',profile_add,name='profile'),
    
    path('category/list', category_list, name='category-list'),
    path('category/<int:category_id>/view', category_view, name='category-view'),
    path('category/<int:category_id>/delete/', category_delete, name='category-delete'),
    


    path('Product/list/',Product_list,name='product-list'),
    path('Product/add/',Product_add,name='product-add'),
    path('Product/<int:Product_id>/view/', Product_view, name='product-view'),
    path('Product/<int:Product_id>/delete/', Product_delete, name='product-delete'),
    path('Product/<int:Product_id>/edit/',Product_edit,name='product-edit'),
    path('category/<int:category_id>/edit2/', category_edit2 ,name='category-edit2'),  
    path('productvariant/list/',ProductVariant_list,name='productvariant_list'),
    path('category/<int:category_id>/products/',CategoryWithProduct.as_view(),name='Category-With-Product'), 
]

