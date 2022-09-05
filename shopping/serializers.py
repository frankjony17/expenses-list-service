from rest_framework import serializers

from shopping.models import Shopping


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
