from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

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
class ProductsListModelViewSet(ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsListSerializer
    pagination_class = None
    http_method_names = ['get']


class ProductsModelViewSet(ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    pagination_class = None
    http_method_names = ['post', 'put', 'delete']

    @swagger_auto_schema(
        tags=['Products'],
        operation_description="Create <b>Products</b> (Used by <b>Shopping</b>)."
    )
    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        tags=['Products'],
        operation_description="Update <b>Products</b> (Used by <b>Shopping</b>)."
    )
    def update(self, request, pk=None, *args, **kwargs):
        instance = self.get_object()
        serializer = self.serializer_class(instance=instance, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        tags=['Products'],
        operation_description="Delete <b>Products</b> (Used by <b>Shopping</b>)."
    )
    def destroy(self, request, pk=None, *args, **kwargs):
        instance = self.get_object()
        serializer = self.serializer_class(instance=instance, data=request.data)

        if serializer.is_valid():
            self.perform_destroy(instance=instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
