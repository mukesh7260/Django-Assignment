from rest_framework import serializers 
from accounts.models import * 

class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = "__all__"
        
class UserProfileModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfileModel 
        fields = "__all__"
        
class UserLoginOtpModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserLoginOtpModel 
        fields = "__all__"
        
class UsercartProductModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsercartProductModel
        fields = "__all__" 
        
class UserCartModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCartModel
        fields = "__all__"