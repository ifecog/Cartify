from django.urls import path
from base.views import product_views as views

urlpatterns = [
    path('', views.get_products, name='products'),
    path('create/', views.create_product, name='create-product'),
    path('top_products/', views.get_top_rated_products, name='top-products'),
    path('<str:pk>/', views.get_product_details, name='product-details'),
    path('<str:pk>/reviews/', views.create_product_review, name='product-reviews'),
    path('update/<str:pk>/', views.update_product, name='update-product'),
    path('delete/<str:pk>/', views.delete_product, name='delete-product'),
]


