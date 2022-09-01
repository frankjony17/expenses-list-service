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

    class Meta:
        model = Products
        fields = ['id', 'name', 'thumbnail', 'description',
                  'estimated_price', 'products_type', 'products_category', 'created_at']


class ProductsListSerializer(ProductsSerializer):
    products_type = ProductsTypeSerializer(many=False)
    products_category = ProductsCategorySerializer(many=False)
