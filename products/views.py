from rest_framework.viewsets import ModelViewSet

from products.models import ProductsType, ProductsCategory, Products
from products.serializers import ProductsTypeSerializer, ProductsCategorySerializer, ProductsSerializer


class ProductsTypeModelViewSet(ModelViewSet):
    queryset = ProductsType.objects.all()
    serializer_class = ProductsTypeSerializer
    pagination_class = None


class ProductsCategoryModelViewSet(ModelViewSet):
    queryset = ProductsCategory.objects.all()
    serializer_class = ProductsCategorySerializer
    pagination_class = None


class ProductsModelViewSet(ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    pagination_class = None
