from django.urls import path
from base.views import product_views as views

urlpatterns = [
    path('', views.get_products, name='products'),
    path('<str:pk>/', views.get_product_details, name='product-details'),
]


# from django.urls import include, path
# from rest_framework import routers
# from base.views.product_views import ProductViewSet

# router = routers.DefaultRouter()
# router.register(r'products', ProductViewSet)

# urlpatterns = [
#     path('', include(router.urls)),
# ]

