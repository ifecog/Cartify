from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

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
    
    page = request.query_params.get('page')
    paginator = Paginator(products, 4)
    
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
        
    if not page:
        page = 1
        
    page = int(page) 
    
    serializer = ProductSerializer(products, many=True)
    
    return Response({'products': serializer.data, 'page': page, 'pages': paginator.num_pages})


@api_view(['GET'])
def get_product_details(request, pk):
    products = Product.objects.get(_id=pk)
    serializer = ProductSerializer(products, many=False)
    
    return Response(serializer.data)



