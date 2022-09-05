from django.db.models import Q
from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework.exceptions import PermissionDenied

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
    model = Products

    def get_queryset(self):
        match self.request.user.has_perm("products.view_products"):
            case True if self.request.user.is_staff:
                self.queryset = self.model.objects.filter(Q(user__is_staff=True))
            case True if not self.request.user.is_staff:
                self.queryset = Products.objects.filter(Q(user=self.request.user.id) |
                                                        Q(user__is_staff=True))
            case _ if not self.swagger_fake_view:
                raise PermissionDenied()

        return self.queryset

    def update(self, request, pk=None, *args, **kwargs):
        products = self.get_model_object(Products, pk=pk)

        match self.request.user.has_perm("products.change_products"):
            case True if request.user == products.user:
                return super().update(request, pk, *args, **kwargs)
            case True if request.user.is_staff and products.user.is_staff:
                return super().update(request, pk, *args, **kwargs)
            case _:
                raise PermissionDenied()

    def destroy(self, request, pk=None, *args, **kwargs):
        products = self.get_model_object(Products, pk=pk)

        match self.request.user.has_perm("products.delete_products"):
            case True if request.user == products.user:
                return super().destroy(request, pk, *args, **kwargs)
            case True if request.user.is_staff and products.user.is_staff:
                return super().destroy(request, pk, *args, **kwargs)
            case _:
                raise PermissionDenied()
