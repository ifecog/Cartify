from django.shortcuts import render

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from base.models import Product
from base.serializers import ProductSerializer



@api_view(['GET'])
def get_products(request):
    query = request.query_params.get('keyword')
    
    if not query:
        query = ''
        
    products = Product.objects.filter(name__icontains=query).order_by('-created_time')
    serializer = ProductSerializer(products, many=True)
    
    return Response(serializer.data)


@api_view(['GET'])
def get_product_details(request, pk):
    products = Product.objects.get(_id=pk)
    serializer = ProductSerializer(products, many=False)
    
    return Response(serializer.data)



