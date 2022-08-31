from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from products.models import ProductsCategory
from products.serializers import ProductsCategorySerializer


@method_decorator(name='list', decorator=swagger_auto_schema(tags=['Products Category']))
@method_decorator(name='retrieve', decorator=swagger_auto_schema(tags=['Products Category']))
class ProductsCategoryModelViewSet(ModelViewSet):
    queryset = ProductsCategory.objects.all()
    serializer_class = ProductsCategorySerializer
    pagination_class = None
    http_method_names = ['get', 'post', ]

    @swagger_auto_schema(tags=['Products Category'])
    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
