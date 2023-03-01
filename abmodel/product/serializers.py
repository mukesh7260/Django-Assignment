from rest_framework import serializers 
from product.models import * 


class ProductMainModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductMainModel
        fields = "__all__" 
        
class ProductImageModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImageModel
        fields = "__all__"