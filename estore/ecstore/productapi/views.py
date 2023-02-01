from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from productapi.models import Products,Reviews,Carts
from rest_framework import status
from productapi.serializers import Productserializers,ProductModelSerializer,UserSerializer,Reviewserializer,CartSerializer
from rest_framework.viewsets import ViewSet,ModelViewSet
from rest_framework import authentication,permissions
from rest_framework.decorators import action


class ProductsView(APIView):
    def get(self,request,*args,**kwargs):
        qs=Products.objects.all()
        serializer=Productserializers(qs,many=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)
    def post(self,request,*args,**kwargs):
        serializer=Productserializers(data=request.data)
        if serializer.is_valid():
            Products.objects.create(**serializer.validated_data)
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class ProductDetailView(APIView):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        qs=Products.objects.get(id=id)
        serializer=Productserializers(qs)
        return Response(data=serializer.data,status=status.HTTP_205_RESET_CONTENT)
    def put(self,request,*args,**kwargs):
        id=kwargs.get("id")
        instance=Products.objects.filter(id=id)
        serializer=Productserializers(data=request.data)
        if serializer.is_valid():


            # instance.save
            instance.update(**serializer.validated_data)
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
         id = kwargs.get("id")
         instance = Products.objects.filter(id=id)
         serializer = Productserializers(data=request.data)
         instance.delete()
         return Response({"msg":"deleted"},status=status.HTTP_204_NO_CONTENT)

class ProductMODELview(APIView):

    def get(self,request,*args,**kwargs):
        qs=Products.objects.all()
        if "category" in request.query_params:
            qs=qs.filter(category__contains=request.query_params.get("category"))
        if "price_gt" in request.query_params:
                qs=qs.filter(price__gte=request.query_params.get("price"))
        serializer=ProductModelSerializer(qs,many=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)
    def post(self,request,*args,**kwargs):
        serializer=ProductModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class ProductDetailModelView(APIView):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        qs=Products.objects.get(id=id)
        serializer=ProductModelSerializer(qs)
        return Response(data=serializer.data,status=status.HTTP_200_OK)
    def put(self,request,*args,**kwargs):
        id=kwargs.get("id")
        object=Products.objects.get(id=id)
        serializer=ProductModelSerializer(data=request.data,instance=object)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,*args,**kwargs):
        id=kwargs.get("id")
        instance=Products.objects.get(id=id)
        # serializer=ProductModelSerializer(data=request.data)
        instance.delete()
        return Response({"msg":"deleted"},status=status.HTTP_204_NO_CONTENT)


class ProductViewsetview(ViewSet):
    def list(self,request,*args,**kwargs):
        qs=Products.objects.all()
        Serializer=ProductModelSerializer(qs,many=True)
        return  Response(data=Serializer.data)


    def create(self,request,*args,**kwargs):
        Serializer=ProductModelSerializer(data=request.data)
        if Serializer.is_valid():
            return Response(data=Serializer.data)
        else:
            return Response(data=Serializer.errors)


    def retrieve(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Products.objects.get(id=id)
        Serializer=ProductModelSerializer(qs)
        return Response(data=Serializer.data)


    def update(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        object=Products.objects.get(id=id)
        serializer=ProductModelSerializer(instance=object,data=request.data)
        if serializer.is_valid():
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)


    def destory(self,request,*args,**kwargs):
        id = kwargs.get("pk")
        instance = Products.objects.get(id=id)
        # serializer=ProductModelSerializer(data=request.data)
        instance.delete()
        return Response({"msg": "deleted"}, status=status.HTTP_204_NO_CONTENT)

class ProductModelViewsetView(ModelViewSet):
    serializer_class = ProductModelSerializer
    queryset = Products.objects.all()
    # authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    @action(methods=["get"],detail=True)
    def get_reviews(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        product=Products.objects.get(id=id)
        reviews=product.reviews_set.all()
        serializer=Reviewserializer(reviews,many=True)
        return Response(data=serializer.data)

    @action(methods=["post"], detail=True)
    def post_reviews(self,request,*args,**kwargs):
        id = kwargs.get("pk")
        product = Products.objects.get(id=id)
        author=request.user
        review=request.data.get("review")
        rating=request.data.get("rating")
        qs=Reviews.objects.create(author=author,
                                  product=product,
                                  review=review,
                                  rating=rating)
        serializer=Reviewserializer(qs)
        return Response(data=serializer.data)
    @action(methods=["post"],detail=True)
    def add_to_cart(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        product=Products.objects.get(id=id)
        user=request.user
        serializer=CartSerializer(data=request.data,context={"user":user,"product":product})
        if serializer.is_valid():
           serializer.save()
           return Response(data=serializer.data)
        else:
           return Response(data=serializer.errors)

class CartView(ModelViewSet):
    serializer_class = CartSerializer
    queryset = Carts.objects.all()
    # authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def list(self,request,*args,**kwargs):
        qs=Carts.objects.filter(User=request.user)
        serializer=CartSerializer(qs,many=True)
        return Response(data=serializer.data)
    def Create(self,request,*args,**kwargs):
        return Response(data={"msg":"no access"})




from  django.contrib.auth.models import User


class UserModelViewset(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()







