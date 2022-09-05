from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework.exceptions import PermissionDenied

from base.views import BaseModelViewSet
from shopping.models import Shopping
from shopping.serializers import ShoppingCreateSerializer, ShoppingSerializer


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
        'default': ShoppingSerializer,
        'create': ShoppingCreateSerializer
    }

    def get_queryset(self):
        if self.request.user.has_perm("shopping.view_shopping"):
            return Shopping.objects.filter(user=self.request.user.id)

        if self.swagger_fake_view:
            return self.queryset

        raise PermissionDenied()

    def create(self, request, *args, **kwargs):
        if self.request.user.has_perm("shopping.add_shopping"):
            return super().create(request, *args, **kwargs)
        raise PermissionDenied()

    def update(self, request, pk=None, *args, **kwargs):
        self.get_model_object(Shopping, pk=pk)

        match self.request.user.has_perm("shopping.change_shopping"):
            case True if request.user == self.instance.user:
                return super().update(request, pk, *args, **kwargs)
            case _:
                raise PermissionDenied()

    def destroy(self, request, pk=None, *args, **kwargs):
        self.get_model_object(Shopping, pk=pk)

        match self.request.user.has_perm("shopping.delete_shopping"):
            case True if request.user == self.instance.user:
                return super().destroy(request, pk, *args, **kwargs)
            case _:
                raise PermissionDenied()
