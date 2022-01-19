from django.shortcuts import render
from rest_framework import generics,status
from rest_framework.response import Response
from .models import User
from . import serializers

# Create your views here.

class HelloAuthView(generics.GenericAPIView):
 def get(self,request):
  return Response(data={"message":"Hello Auth"},status=status.HTTP_200_OK)


class UserCreateView(generics.GenericApiView):
 
 def post(self,request):
  
 