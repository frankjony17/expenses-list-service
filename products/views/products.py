from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework.viewsets import ModelViewSet

from products.models import Products
from products.serializers import ProductsSerializer


@method_decorator(name='list', decorator=swagger_auto_schema(tags=['Products']))
class ProductsModelViewSet(ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    pagination_class = None
