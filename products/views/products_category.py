from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema

from base.views import BaseModelViewSet
from products.models import ProductsCategory
from products.serializers import ProductsCategorySerializer


@method_decorator(name='list', decorator=swagger_auto_schema(
    tags=['Products Category'],
    operation_description="List of <b>Categories</b> (Used by <b>Product</b> and <b>Expenses</b>)."
))
@method_decorator(name='retrieve', decorator=swagger_auto_schema(
    tags=['Products Category'],
    operation_description="Retrieve <b>Category</b> by <b>Id</b> "
                          "(Used by <b>Product</b> and <b>Expenses</b>)."
))
@method_decorator(name='create', decorator=swagger_auto_schema(
    tags=['Products Category'],
    operation_description="Create <b>ProductsCategory</b>"
                          "(Used by <b>Product</b> and <b>Expenses</b>)."
))
@method_decorator(name='update', decorator=swagger_auto_schema(
    tags=['Products Category'],
    operation_description="Update <b>ProductsCategory</b> "
                          "(Used by <b>Product</b> and <b>Expenses</b>)."
))
@method_decorator(name='destroy', decorator=swagger_auto_schema(
    tags=['Products Category'],
    operation_description="Delete <b>ProductsCategory</b> "
                          "(Used by <b>Product</b> and <b>Expenses</b>)."
))
class ProductsCategoryModelViewSet(BaseModelViewSet):
    queryset = ProductsCategory.objects.all()
    serializers = {
        'default': ProductsCategorySerializer
    }
