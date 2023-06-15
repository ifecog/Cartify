from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from base.models import Product, Review
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
def get_top_rated_products(request):
    products = Product.objects.filter(rating__gte=4).order_by('-rating')[0:5]
    serializer = ProductSerializer(products, many=True)
    
    return Response(serializer.data)


@api_view(['GET'])
def get_product_details(request, pk):
    products = Product.objects.get(_id=pk)
    serializer = ProductSerializer(products, many=False)
    
    return Response(serializer.data)

@api_view(['POST'])
def upload_image(request):
    data = request.data
    
    product_id = data['product_id']
    product = Product.objects.get(_id=product_id)
    
    product.image = request.FILES.get('image')
    product.save()
    
    return Response('Image was successfully uploaded!')


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_product_review(request, pk):
    user = request.user
    product = Product.objects.get(_id=pk)
    data = request.data
    
    # 1. Review already exists from customer
    already_exists = product.review_set.filter(user=user).exists()
    
    if already_exists:
        message = {'detail': 'Product already reviewed by user'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)

    # 2. No rating or 0 rating
    elif data['rating'] == 0:
        message = {'detail': 'Kindly select a rating'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)

    # 3. Create rating
    else:
        review = Review.objects.create(
            user=user,
            product=product,
            name=user.first_name,
            rating=data['rating'],
            comment=data['comment'],
        )
        
        reviews = product.review_set.all()
        product.num_of_reviews = len(reviews)
        
        total = 0
        for i in reviews:
            total += i.rating
            
        product.rating = total / len(reviews)
        product.save()
    
        return Response('review added')
        # return Response({'details': 'Review added'}, status=status.HTTP_201_CREATED)

@api_view(['POST'])
@permission_classes([IsAdminUser])
def create_product(request):
    user = request.user
    product = Product.objects.create(
        user=user,
        name='Sample Name',
        price=0,
        brand='Sample Brand',
        count_in_stock=0,
        category='Sample Category',
        description='',
    )
    serializer = ProductSerializer(product, many=False)
    
    return Response(serializer.data)

@api_view(['PUT'])
@permission_classes([IsAdminUser])
def update_product(request, pk):
    product = Product.objects.get(_id=pk)
    data = request.data
    
    # update fields
    product.name=data['name']
    product.description=data['description']
    product.price=data['price']
    product.brand=data['brand']
    product.category=data['category']
    product.count_in_stock=data['count_in_stock']
    
    product.save()
    
    serializer = ProductSerializer(product, many=False)
    
    return Response(serializer.data)

@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def delete_product(request, pk):
    product = Product.objects.get(_id=pk)
    product.delete()
    
    return Response('Product was successfully deleted')