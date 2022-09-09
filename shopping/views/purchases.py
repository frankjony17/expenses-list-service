from django.core.exceptions import ObjectDoesNotExist
from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response

from base.views import BaseModelViewSet
from products.models import Products
from shopping.models import Purchases
from shopping.serializers import PurchasesCreateSerializer, PurchasesListSerializer


@method_decorator(name='list', decorator=swagger_auto_schema(
    tags=['Purchases'],
    operation_description="List of <b>Purchases</b>."
))
@method_decorator(name='retrieve', decorator=swagger_auto_schema(
    tags=['Purchases'],
    operation_description="Retrieve <b>Purchases</b> by <b>Id</b>."
))
@method_decorator(name='create', decorator=swagger_auto_schema(
    tags=['Purchases'],
    operation_description="Create <b>Purchases</b>."
))
@method_decorator(name='update', decorator=swagger_auto_schema(
    tags=['Purchases'],
    operation_description="Update <b>Purchases</b>."
))
@method_decorator(name='destroy', decorator=swagger_auto_schema(
    tags=['Purchases'],
    operation_description="Delete <b>Purchases</b>."
))
class PurchasesModelViewSet(BaseModelViewSet):
    serializers = {
        'default': PurchasesListSerializer,
        'create': PurchasesCreateSerializer
    }

    def get_queryset(self):
        if self.request.user.has_perm("shopping.view_purchases"):
            return Purchases.objects.filter(shopping__user_id=self.request.user.id)
        self.raise_list_permission_denied()

    def create(self, request, *args, **kwargs):
        if not self.request.user.has_perm("shopping.add_purchases"):
            raise PermissionDenied()

        try:
            products = Products.objects.get(pk=request.data.get("products"))

            if products:
                request.data["price"] = products.estimated_price
                return super().create(request, *args, **kwargs)
        except ObjectDoesNotExist as exc:
            return Response(data={"products": [str(exc)]}, status=status.HTTP_400_BAD_REQUEST)
