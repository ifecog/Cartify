from django.urls import path
from base.views import user_views as views

urlpatterns = [
    path('', views.get_users, name='users'),
    path('register/', views.register_user, name='register'),
    path('login/', views.MyTokenObtainPairView.as_view(), name='token-obtain-pair'),
    path('profile/', views.get_user_profile, name='user-profile'),
    path('profile/update/', views.update_user_profile, name='update-profile'),
    path('<str:pk>/', views.get_user_by_id, name='get-user'),
    path('update/<str:pk>/', views.update_user, name='update-user'),
    path('delete/<str:pk>/', views.delete_user, name='delete-user'),

]