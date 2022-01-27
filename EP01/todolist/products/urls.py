from django.urls import path
from . import views


urlpatterns = [
    # Ans1: APIView
    path('APIView/get_product/', views.ApiViewAllProducts.as_view(), name='get_products'),
    path('APIView/get_product/<int:pk>/', views.ApiViewProductsById.as_view(), name='get_products'),
    # Ans2: generics APIs View
    path('generics/get_product/', views.GenericsProductsListCreate.as_view(), name='get_products'),
    path('generics/get_product/<int:pk>/', views.GenericsProductsById.as_view(), name='get_products_by_id'),
]