from django.shortcuts import render
from rest_framework.decorators import api_view,APIView
from rest_framework.response import Response
from .models import *
from .serializer import *
from rest_framework import status

# Create your views here.

@api_view(['GET']) 
def Category_list(request):
    if request.method == 'GET':
        category=Category.objects.all()
        serializer = CategorySerializer(category,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
@api_view(['GET'])
def Product_list(request):
    if request.method == 'GET':
        product=Product.objects.all()
        serializer=ProductSerializer(product,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
@api_view(['GET'])
def Size_list(request):
    if request.method == 'GET':
        size=Size.objects.all()
        serializer=SizeSerializer(size,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    
@api_view(['GET'])
def Size_list_one(request,size_id):
    if request.method == 'GET':
        size=Size.objects.get(id=size_id)
        serializer=SizeSerializer(size)
        return Response(serializer.data,status=status.HTTP_200_OK)