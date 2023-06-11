from django.urls import path
from base.views import product_views as views

urlpatterns = [
    path('', views.get_products, name='products'),
    path('top_products/', views.get_top_rated_products, name='top-products'),
    path('<str:pk>/', views.get_product_details, name='product-details'),
]


