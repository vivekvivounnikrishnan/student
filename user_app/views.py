from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view,APIView
from rest_framework import status
from .models import *
from .serializers import *
from .models import *
# Create your views here.

############################################################### GET ###################################################################
# @api_view(['GET'])
# def login_list(request):
#     if request.method == 'GET':
#         login = Login.objects.all()
#         serializer = LoginSerializer(login, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
################################################################ GET AND POST ###########################################################
    
# @api_view(['GET','POST'])
# def profile_add(request):
#     if request.method == 'GET':
#         login = Login.objects.all()
#         serializer = LoginSerializer(login, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     elif request.method == 'POST':
#         serializers = LoginSerializer(data=request.data)
#         if serializers.is_valid():
#             serializers.save()
#             return Response(serializers.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
def category_view(request, category_id):
    category = Category.objects.get(id=category_id)
    if request.method ==  'GET':
        serializer = CategorySerializer(category, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET', 'DELETE'])
def category_delete(request, category_id):
    category = Category.objects.get(id=category_id)
    if request.method ==  'GET':
        serializer = CategorySerializer(category, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'DELETE':
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
    
@api_view(['GET'])
def category_list(request):
    if request.method == 'GET':
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


##################################################################### PRODUCT TABLE (ADD/LIST/VIEW/DELETE) #######################################################################


@api_view(['GET'])
def Product_list(request):
    if request.method == 'GET':
        product = Product.objects.all()
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
@api_view(['GET','POST'])
def Product_add(request):
    if request.method == 'GET':
        product = Product.objects.all()
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        serializers = ProductSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    
@api_view(['GET'])
def Product_view(request, Product_id):
    product = Product.objects.get(id=Product_id)
    if request.method ==  'GET':
        serializer = ProductSerializer(product, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET', 'DELETE'])
def Product_delete(request, Product_id):
    product = Product.objects.get(id=Product_id)
    if request.method ==  'GET':
        serializer = ProductSerializer(product, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
      
################################################################## GET AND PATCH #################################################################


@api_view(['GET', 'PATCH'])
def Product_edit(request, Product_id):
    try:
       product = Product.objects.get(id=Product_id)
    except Product.DoesNotExist:
        return Response({'error': 'personalinformation not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer =ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    elif request.method == 'PATCH':
        serializer = ProductSerializer(product, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

######################################################################## PUT ####################################################################
 
@api_view(['GET', 'PUT'])
def category_edit2(request, category_id):
    try:
        category = Category.objects.get(id=category_id)
    except Category.DoesNotExist:
        return Response({'error': 'Category not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CategorySerializer(category)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    elif request.method == 'PUT':
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
@api_view(['GET'])
def ProductVariant_list(request):
    if request.method == 'GET':
        category = ProductVariant.objects.all()
        serializer = ProductVariantSerializer(category,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
class CategoryWithProduct(APIView):
    def get(self, respect,category_id, format=None):
        try:
            category = Categorycloth.objects.get(id=category_id)
        except Categorycloth.DoesNotExist:
            return Response({'error': 'Category not found '}, status=status.HTTP_404_NOT_FOUND)
        
        category_serializer = CategorySerializer(category)
        products = Productcloth.objects.filter(category=category)
        final_data = [ ]
        for product in products:
          products_serializer = ProductSerializer(product)
          product_variants = ProductVariant.objects.filter(product=product)
          variant_serializer = ProductVariantSerializer(product_variants, many=True)
          final_data.append({'product':products_serializer.data,'variant':variant_serializer.data})
        
        response_data ={
                        'category': category_serializer.data,
                        'products':final_data,
        }

        return Response(response_data,status=status.HTTP_200_OK)

