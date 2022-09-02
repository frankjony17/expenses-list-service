from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema

from base.views import BaseModelViewSet
from shopping.models import Shopping
from shopping.serializers import ShoppingSerializer


@method_decorator(name='list', decorator=swagger_auto_schema(
    tags=['Shopping'],
    operation_description="List of <b>Shopping</b>."
))
@method_decorator(name='retrieve', decorator=swagger_auto_schema(
    tags=['Shopping'],
    operation_description="Retrieve <b>Shopping</b> by <b>Id</b>."
))
@method_decorator(name='create', decorator=swagger_auto_schema(
    tags=['Shopping'],
    operation_description="Create <b>Shopping</b>."
))
@method_decorator(name='update', decorator=swagger_auto_schema(
    tags=['Shopping'],
    operation_description="Update <b>Shopping</b>."
))
@method_decorator(name='destroy', decorator=swagger_auto_schema(
    tags=['Shopping'],
    operation_description="Delete <b>Shopping</b>."
))
class ShoppingModelViewSet(BaseModelViewSet):
    queryset = Shopping.objects.all()
    serializers = {
        'default': ShoppingSerializer
    }
