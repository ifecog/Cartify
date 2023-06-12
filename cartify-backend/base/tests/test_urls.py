from django.test import SimpleTestCase
from django.urls import resolve, reverse
from base.views.product_views import (
    get_products,
    get_product_details,
)
from base.views.user_views import (
    get_users,
    register_user,
    MyTokenObtainPairView,
    get_user_profile,
)

class TestProductUrls(SimpleTestCase):
    
    def test_products_url_is_resolved(self):
        url = reverse('products')
        self.assertEquals(resolve(url).func, get_products)

    def test_product_details_url_is_resolved(self):
        url = reverse('product-details', args=['some-slug'])
        self.assertEquals(resolve(url).func, get_product_details)
        

class TestUserUrls(SimpleTestCase):
    
    def test_users_url_is_resolved(self):
        url = reverse('users')
        self.assertEquals(resolve(url).func, get_users)
        
    def test_user_register_url_is_resolved(self):
        url = reverse('register')
        self.assertEquals(resolve(url).func, register_user)
        
    def test_login_user_is_resolved(self):
        url = reverse('token-obtain-pair')
        self.assertEquals(resolve(url).func.view_class, MyTokenObtainPairView)

    def test_user_profile_url_is_resolved(self):
        url = reverse('user-profile')
        self.assertEquals(resolve(url).func, get_user_profile)

