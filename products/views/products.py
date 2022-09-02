from django.db.models import Q
from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema

from base.views import BaseModelViewSet
from products.models import Products
from products.serializers import ProductsListSerializer, ProductsSerializer


@method_decorator(name='list', decorator=swagger_auto_schema(
    tags=['Products'],
    operation_description="List of <b>Products</b> with <b>Category</b> and <b>ProductsType</b>."
))
@method_decorator(name='retrieve', decorator=swagger_auto_schema(
    tags=['Products'],
    operation_description="Retrieve <b>Products</b> by <b>Id</b> (Used by <b>Shopping</b>)."
))
@method_decorator(name='create', decorator=swagger_auto_schema(
    tags=['Products'],
    operation_description="Create <b>Products</b> (Used by <b>Shopping</b>)."
))
@method_decorator(name='update', decorator=swagger_auto_schema(
    tags=['Products'],
    operation_description="Update <b>Products</b> (Used by <b>Shopping</b>)."
))
@method_decorator(name='destroy', decorator=swagger_auto_schema(
    tags=['Products'],
    operation_description="Delete <b>Products</b> (Used by <b>Shopping</b>)."
))
class ProductsModelViewSet(BaseModelViewSet):
    serializers = {
        'default': ProductsSerializer,
        'list': ProductsListSerializer,
        'retrieve': ProductsListSerializer
    }

    def get_queryset(self):
        self.queryset = Products.objects.filter(Q(user=self.request.user.id) | Q(user=None))
        return self.queryset
