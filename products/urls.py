from django.urls import path
from rest_framework import routers

from products.views.products import ProductsModelViewSet
from products.views.products_category import ProductsCategoryModelViewSet
from products.views.products_type import ProductsTypeModelViewSet


router = routers.DefaultRouter()
# products-type
router.register(r'type', ProductsTypeModelViewSet, basename="products_type")
# products-category
router.register(r'category', ProductsCategoryModelViewSet, basename="products_category")


urlpatterns = [
    # Products
    path('', ProductsModelViewSet.as_view({'get': 'list'}), name='products'),
] + router.urls
