from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test Api views"""
    def get(self,request,format=None):
        """Return a LIst of APIViews features"""
        an_apiview=[
            'uses HTTP methods as function (get,post,patch,put,delete)',
            'Is similar to a traditional Django View',
            'Gives you control over application logic',
            'is mapped manually to URLs',
        ]

        return Response({"message":"Hello",'an_apiview':an_apiview})