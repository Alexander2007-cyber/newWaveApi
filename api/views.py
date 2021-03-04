from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .userSer import UserSerializer
from .models import User

# Create your views here.


class ApiOverview(APIView):
    def get(self, request, format=None):
        data = User.objects.all()
        data = UserSerializer(data, many=True).data
        return Response(data)

class CreateView(APIView):
    def post(self, request, format=None):
        serr = UserSerializer(data=request.data)
        if serr.is_valid():
            serr.save()
        else: 
            print("error")
        
        return Response(serr.data)