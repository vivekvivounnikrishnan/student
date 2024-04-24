from django.shortcuts import render
from rest_framework.decorators import api_view,APIView
from rest_framework.response import Response

# Create your views here.
from studentapp.serializers import SchoolSerializer
from .models import *
from .serializers import *
from rest_framework import status


@api_view(['GET'])
def School_list(request):
    if request.method == 'GET':
        school=School.objects.all()
        serializer = SchoolSerializer(school,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
@api_view(['GET','POST'])
def School_add(request):
    
    
    if request.method == 'GET':
        school=School.objects.all()
        serializer = SchoolSerializer(school,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        serializer = SchoolSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
#################################################################################################################################################
    
@api_view(['GET'])
def School_view(request, category_id):
    school = School.objects.get(id=category_id)
    if request.method ==  'GET':
        serializer = SchoolSerializer(school, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET', 'DELETE'])
def School_delete(request, school_id):
    school = School.objects.get(id=school_id)
    if request.method ==  'GET':
        serializer = SchoolSerializer(school, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'DELETE':
        school.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
############################################################### BATCH #############################################################################  

@api_view(['GET'])
def Batch_list(request):
    if request.method == 'GET':
        batch=Batch.objects.all()
        serializer = BatchSerializer(batch,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
@api_view(['GET','POST'])
def Batch_add(request):
    if request.method == 'GET':
        batch=Batch.objects.all()
        serializer = BatchSerializer(batch,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        serializer = BatchSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)   