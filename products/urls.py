from django.urls import path

from products import views

urlpatterns = [
    path('type/', views.ProductsTypeModelViewSet.as_view({'get': 'list'}), name='products_type'),
    path('category/', views.ProductsCategoryModelViewSet.as_view({'get': 'list'}), name='products_category'),
    # Products
    path('', views.ProductsModelViewSet.as_view({'get': 'list'}), name='products'),
]
