from django.shortcuts import render
from rest_framework.views import APIView
from accounts.models import *
from accounts.serializers import * 
from rest_framework.response import Response 


class Details(APIView):
    def get(self, request, pk=None, format=None):
        phone = UserModel.objects.get(id=pk)
        nm = phone.phone_number
        name = UserProfileModel.objects.all()
        serializer = UserProfileModelSerializer(name,many=True)
        cart = UserCartModel.objects.all()
        serializer1 = UserCartModelSerializer(cart,many=True)
        return Response({'phone_number':nm,'name':serializer.data,'user_cart':serializer1.data})
        
    def post(self, request, format=None):
        serializer = UserModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'}) 

 
 
