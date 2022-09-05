from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework.exceptions import PermissionDenied

from base.views import BaseModelViewSet
from products.models import ProductsType
from products.serializers import ProductsTypeSerializer


@method_decorator(name='list', decorator=swagger_auto_schema(
    tags=['Products Type'],
    operation_description="List of <b>ProductsType</b> (Used by <b>Product</b>)."
))
@method_decorator(name='retrieve', decorator=swagger_auto_schema(
    tags=['Products Type'],
    operation_description="Retrieve <b>ProductsType</b> by <b>id</b> (Used by <b>Product</b>)."
))
@method_decorator(name='create', decorator=swagger_auto_schema(
        tags=['Products Type'],
        operation_description="Create <b>ProductsType</b> (Used by <b>Product</b>)."
))
@method_decorator(name='update', decorator=swagger_auto_schema(
        tags=['Products Type'],
        operation_description="Update <b>ProductsType</b> (Used by <b>Products</b>)."
))
@method_decorator(name='destroy', decorator=swagger_auto_schema(
        tags=['Products Type'],
        operation_description="Delete <b>ProductsType</b> (Used by <b>Products</b>)."
))
class ProductsTypeModelViewSet(BaseModelViewSet):
    queryset = ProductsType.objects.all()
    serializers = {
        'default': ProductsTypeSerializer
    }

    def create(self, request, *args, **kwargs):
        if self.request.user.is_staff:
            return super().create(request, *args, **kwargs)
        raise PermissionDenied()

    def update(self, request, pk=None, *args, **kwargs):
        if self.request.user.is_staff:
            return super().update(request, pk, *args, **kwargs)
        raise PermissionDenied()

    def destroy(self, request, pk=None, *args, **kwargs):
        if self.request.user.is_staff:
            return super().destroy(request, pk, *args, **kwargs)
        raise PermissionDenied()
