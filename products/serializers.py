from rest_framework import serializers

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
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

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
            'user'
        ]


class ProductsListSerializer(ProductsSerializer):
    products_type = ProductsTypeSerializer(many=False)
    products_category = ProductsCategorySerializer(many=False)
