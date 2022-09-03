from rest_framework import serializers

from api_auth.serializers import UserStaffSerializer
from products.models import Products, ProductsCategory, ProductsType


class ProductsTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductsType
        fields = ['id', 'type', 'description']


class ProductsCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductsCategory
        fields = ['id', 'category', 'description']


class ProductsSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Products
        fields = [
            'id',
            'name',
            'thumbnail',
            'description',
            'estimated_price',
            'products_type',
            'products_category',
            'owner'
        ]


class ProductsListSerializer(ProductsSerializer):
    products_type = ProductsTypeSerializer(many=False)
    products_category = ProductsCategorySerializer(many=False)
    owner = UserStaffSerializer(many=False, read_only=True)
