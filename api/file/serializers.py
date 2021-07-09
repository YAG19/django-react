from rest_framework import serializers

from .models import Product

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    file = serializers.FileField(
        max_length=None , allow_null=False, required=True
    )

    class Meta:
        model = Product
        fields = ("name","file")