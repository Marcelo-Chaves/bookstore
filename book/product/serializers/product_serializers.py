from rest_framework import serializers

from product.models.product import Product
from product.serializers.catergory_serilizer import CategorySerializer

from book.product.models import product


class ProductSerilizer(serializers.ModelSerilizers):
    category =CategorySerializer(required=True, many=True)


    class Meta:
        model = product
        fields = [
            'title',
            'description',
            'price',
            'category',
        ]