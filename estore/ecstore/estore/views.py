from django.shortcuts import render

# Create your views here.
from estore.models import products
from rest_framework.views import APIView
from rest_framework.response import Response


class ProductView(APIView):
    def get(self,request,*args,**kwargs):
        if "price" in request.query_params:
            # id=int((request.query_params.get("price")))
            data=[p for p in products if p["price"]>50]
            return Response(data=data)
        data=request.data.get("products")
        return Response(data=products)
    def post(self,request,*args,**kwargs):
        data=request.data
        products.append(data)
        return Response(data=products)

