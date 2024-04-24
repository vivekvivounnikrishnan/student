from django.urls import path
from studentapp.views import *

urlpatterns = [
    path('school/list/',School_list,name='School-list'),
    path('School/add/',School_add,name=' School-add'),
    path('school/view/<int:school_id>/view/', School_view, name='school-view'),
    path('school/delete/<int:school_id>/delete/', School_delete, name='school-delete'),
    
    path('batch/list/',Batch_list,name='Batch-list'),
    path('batch/add/',Batch_add,name='Batch-add'),
]
