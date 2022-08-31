
from rest_framework import serializers

from products.models import ProductsType, ProductsCategory, Products


class ProductsTypeSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        return ProductsType.objects.create(**validated_data)

    class Meta:
        model = ProductsType
        fields = ['id', 'type', 'description']


class ProductsCategorySerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        return ProductsCategory.objects.create(**validated_data)

    class Meta:
        model = ProductsCategory
        fields = ['id', 'category', 'description']


class ProductsSerializer(serializers.ModelSerializer):
    products_type = ProductsTypeSerializer()
    products_category = ProductsCategorySerializer()

    class Meta:
        model = Products
        fields = ['id', 'name', 'thumbnail', 'description',
                  'estimated_price', 'products_type', 'products_category', 'created_at']
