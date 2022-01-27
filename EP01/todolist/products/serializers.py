from rest_framework import serializers
from .models import ProductsModel


class ProductsSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        return ProductsModel.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.product_type = validated_data.get('product_type', instance.product_type)
        instance.name = validated_data.get('name', instance.name)
        instance.price = validated_data.get('price', instance.price)
        instance.unit = validated_data.get('unit', instance.unit)

        instance.save()
        return instance

    class Meta:
        model = ProductsModel
        fields = '__all__'
