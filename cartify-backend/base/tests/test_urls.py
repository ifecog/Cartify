from django.test import SimpleTestCase
from django.urls import resolve, reverse
from base.views.product_views import (
    get_products,
    get_product_details,
)

class TestProductUrls(SimpleTestCase):
    
    def test_products_url_is_resolved(self):
        url = reverse('products')
        self.assertEquals(resolve(url).func, get_products)

    def test_product_details_url_is_resolved(self):
        url = reverse('product-details', args=['some-slug'])
        self.assertEquals(resolve(url).func, get_product_details)

