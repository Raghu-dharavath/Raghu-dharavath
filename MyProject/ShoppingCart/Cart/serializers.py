from rest_framework import serializers
from .models import Product

# class ProductSerializer(serializers.Serializer):
#     id = serializers.IntegerField(label="enter Product id")
#     name = serializers.CharField(label="enter Product name")
#     sku = serializers.CharField(label="sku name")
#     price = serializers.FloatField(label="enter price")
#     quantity_in_stock = serializers.IntegerField(label ="enter quantity")

class ProductSerializer(serializers.Serializer):
    class Meta:
        model = Product
        fields = '__all__'