from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from base.models import (
    Product,
)
from django.contrib.auth.models import User

class TestProductViews(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.products_url = reverse('products')
        self.toprated_products_url = reverse('top-products')
        self.product_detail_url = reverse('product-details', args=[1])        
               
    def test_get_products_GET(self):
        response = self.client.get(self.products_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_toprated_products_GET(self):
        response = self.client.get(self.toprated_products_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_product_detail_GET(self):
        # Create a sample product for testing
        sample_product = Product.objects.create(_id=1, name='Sample Product')
        
        response = self.client.get(self.product_detail_url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Sample Product')

# class TestUserViews(TestCase):
    
#     def setUp(self):
#         self.client = Client()
#         self.users_url = reverse('users')
               
#     def test_get_users_GET(self):
#         response = self.client.get(self.users_url)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
