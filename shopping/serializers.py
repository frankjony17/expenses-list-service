from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from products.serializers import ProductsSerializer
from shopping.models import Shopping, Purchases


class ShoppingSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Shopping
        fields = [
            'id',
            'description',
            'purchase_date',
            'amount_available',
            'approximate_cost',
            'final_amount',
            'created_at',
            'user'
        ]


class ShoppingCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Shopping
        fields = [
            'id',
            'description',
            'amount_available',
            'user'
        ]


class PurchasesCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchases
        fields = [
            'id',
            'shopping',
            'products',
            'price'
        ]


class PurchasesListSerializer(serializers.ModelSerializer):
    products = ProductsSerializer(many=False)
    shopping = ShoppingSerializer(many=False)

    class Meta:
        model = Purchases
        fields = [
            'id',
            'products',
            'quantity',
            'price',
            'price_date',
            'unit',
            'shopping',
            'checked',
            'created_at'
        ]
