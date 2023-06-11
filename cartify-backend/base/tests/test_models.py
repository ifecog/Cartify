from django.test import TestCase
from django.contrib.auth.models import User
from base.models import Product, Review, Order, OrderItem, ShippingAddress


class ModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.product = Product.objects.create(
            user=self.user,
            name='Test Product',
            brand='Test Brand',
            category='Test Category',
            description='Test Description',
            price=10.0,
            count_in_stock=100
        )
        self.order = Order.objects.create(
            user=self.user,
            payment_method='Test Payment Method',
            tax_price=1.0,
            shipping_price=2.0,
            total_price=13.0,
            is_paid=True,
            is_delivered=False
        )
        self.order_item = OrderItem.objects.create(
            product=self.product,
            order=self.order,
            name='Test Order Item',
            qty=2,
            price=5.0,
            image='test_image.jpg'
        )
        self.shipping_address = ShippingAddress.objects.create(
            order=self.order,
            country='Test Country',
            city='Test City',
            address='Test Address',
            postal_code='12345'
        )
        self.review = Review.objects.create(
            product=self.product,
            user=self.user,
            name='Test Review',
            rating=4,
            comment='Test Comment'
        )

    def test_product_model(self):
        self.assertEqual(str(self.product), 'Test Product')

    def test_review_model(self):
        self.assertEqual(str(self.review), '4')

    def test_order_model(self):
        self.assertEqual(str(self.order), str(self.order.created_time))

    def test_order_item_model(self):
        self.assertEqual(str(self.order_item), 'Test Order Item')

    def test_shipping_address_model(self):
        self.assertEqual(str(self.shipping_address), 'Test Address')


