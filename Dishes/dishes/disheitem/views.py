from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from disheitem.models import Dishes
from rest_framework import status
from disheitem.serializer import Dishserializer,Dishemodelserializer
from rest_framework.viewsets import ViewSet

class DishesView(APIView):
    def get(self,request,*args,**kwargs):
        qs=Dishes.objects.all()
        serializer=Dishserializer(qs,many=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)
    def post(self,request,*args,**kwargs):
        serializer=Dishserializer(data=request.data)
        if serializer.is_valid():
            Dishes.objects.create(**serializer.validated_data)
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class DishesDetailsview(APIView):
    def get(self, request, *args, **kwargs):
        id = kwargs.get("id")
        qs = Dishes.objects.get(id=id)
        serializer = Dishserializer(qs)
        return Response(data=serializer.data,status=status.HTTP_205_RESET_CONTENT)

    def put(self, request, *args, **kwargs):
        id = kwargs.get("id")
        instance =Dishes.objects.filter(id=id)
        serializer = Dishserializer(data=request.data)
        if serializer.is_valid():

            # instance.save
            instance.update(**serializer.validated_data)
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        id = kwargs.get("id")

        instance = Dishes.objects.get(id=id)
        serializer = Dishserializer(instance)
        instance.delete()
        return Response({"msg": "delete"}, status=status.HTTP_204_NO_CONTENT)

# Create your views here.

class DishesDetailsview(APIView):
    def get(self,request,*args,**kwargs):
        qs=Dishes.objects.all()
        serializer=Dishserializer(qs,many=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)
    def post(self,request,*args,**kwargs):
        serializer=Dishserializer(data=request.data)
        if serializer.is_valid():
            Dishes.objects.create(**serializer.validated_data)
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class DishesDetailsview(APIView):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        qs=Dishes.objects.get(id=id)
        serializer=Dishserializer(qs)
        return Response(data=serializer.data,status=status.HTTP_205_RESET_CONTENT)
    def put(self,request,*args,**kwargs):
        id=kwargs.get("id")
        instance=Dishes.objects.filter(id=id)
        serializer=Dishserializer(data=request.data)
        if serializer.is_valid():


            # instance.save
            instance.update(**serializer.validated_data)
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
         id = kwargs.get("id")
         instance = Dishes.objects.filter(id=id)
         serializer =Dishserializer(data=request.data)
         instance.delete()
         return Response({"msg":"deleted"},status=status.HTTP_204_NO_CONTENT)

class Dishemodelview(APIView):

    def get(self,request,*args,**kwargs):
        qs=Dishes.objects.all()
        if "category" in request.query_params:
            qs=qs.filter(category__contains=request.query_params.get("category"))
        if "price_gt" in request.query_params:
                qs=qs.filter(price__gte=request.query_params.get("price"))
        serializer=Dishemodelserializer(qs,many=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)
    def post(self,request,*args,**kwargs):
        serializer=Dishemodelserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class DishDetailModelView(APIView):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        qs=Dishes.objects.get(id=id)
        serializer=Dishemodelserializer(qs)
        return Response(data=serializer.data,status=status.HTTP_200_OK)
    def put(self,request,*args,**kwargs):
        id=kwargs.get("id")
        object=Dishes.objects.get(id=id)
        serializer=Dishemodelserializer(data=request.data,instance=object)
        if serializer.is_valid():
            serializer.save()

            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,*args,**kwargs):
        id=kwargs.get("id")
        instance=Dishes.objects.get(id=id)
        # serializer=DishDetailModelView(data=request.data)
        instance.delete()
        return Response({"msg":"deleted"},status=status.HTTP_204_NO_CONTENT)

class Disheviewsetview(ViewSet):
    def list(self,request,*args,**kwargs):
        qs=Dishes.objects.all()
        serializer=Dishemodelserializer(qs,many=True)
        return Response(data=serializer.data)

    def create(self,request,*args,**kwargs):
        serializer=Dishemodelserializer(data=request.data)
        if serializer.is_valid():
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

    def retrieve(self,request,*args,**kwargs):
        id = kwargs.get("pk")
        qs = Dishes.objects.get(id=id)
        Serializer =Dishemodelserializer(qs)
        return Response(data=Serializer.data)

    def update(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        object = Dishes.objects.get(id=id)
        serializer = Dishemodelserializer(instance=object, data=request.data)
        if serializer.is_valid():
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

    def destory(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        instance =Dishes.objects.get(id=id)
            # serializer=ProductModelSerializer(data=request.data)
        instance.delete()
        return Response({"msg": "deleted"}, status=status.HTTP_204_NO_CONTENT)



