from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response


items = ["Book1", "Book2", "Book3", "Book4"]

class ListView(APIView):

    def get(self, request):
        return Response(items, status=status.HTTP_200_OK)
    
class AddView(APIView):

    def post(self, request):
        data = request.data
        items.extend(data.get("data",[]))
        return Response(data, status=status.HTTP_201_CREATED)
