from django.shortcuts import render
from rest_framework.response import Response
from  rest_framework.viewsets import ModelViewSet
from  socialapp.serializer import Userserializer,UserProfileSerializer,PostSerializer,CommentSerializer
from django.contrib.auth.models import User
from socialapp.models import UserProfile,Posts,comment
from rest_framework import permissions
from rest_framework.decorators import action


class UserRegisterationview(ModelViewSet):
    serializer_class = Userserializer
    queryset = User.objects.all()

# Create your views here.


class UserProfileView(ModelViewSet):
    serializer_class=UserProfileSerializer
    queryset=UserProfile.objects.all()
    permission_classes=[permissions.IsAuthenticated]

    def create(self,request,*args,**kwargs):
        serializer=UserProfileSerializer(data=request.data,context={"user":request.user})
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

class PostView(ModelViewSet):
    serializer_class =PostSerializer
    queryset = Posts.objects.all()
    permissions_class=[permissions.IsAuthenticated]

    def perform_create(self,serializer):
        serializer.save(author=self.request.user)
    @action(methods=["post"],detail=True)
    def add_comment(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        post=Posts.objects.get(id=id)
        user=request.user
        serializer=CommentSerializer(data=request.data,context={"post":post,"user":user})

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)





