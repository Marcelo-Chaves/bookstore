from rest_framework import serializers

from product.models.category import Category

class CategorySerializer(serializers.ModelSerilizer):
    class Meta:
        model = Category
        fields= [
            'title',
            'slug',
            'description',
            'active',
        ]
