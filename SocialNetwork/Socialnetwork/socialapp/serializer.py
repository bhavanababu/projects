from rest_framework import serializers
from django.contrib.auth.models import User
from socialapp.models import UserProfile,Posts,comment

class Userserializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=[
            "username",
            "email",
            "password"
        ]
    def create(self,validated_data):
            return User.objects.create_user(**validated_data)

class UserProfileSerializer(serializers.ModelSerializer):
    user=serializers.CharField(read_only=True)
    class Meta:
        model=UserProfile
        fields=[
                "user",
                "ProfilePic",
                "DOB",
                "gender",
                "address",
                "bio",
                "cover_pic"]
    def create(self,validated_data):
        user=self.context.get("user")
        return UserProfile.objects.create(user=user,**validated_data)

class PostSerializer(serializers.ModelSerializer):
    author=serializers.CharField(read_only=True)
    class Meta:
        model=Posts
        exclude=("liked_by",)

class CommentSerializer(serializers.ModelSerializer):
    user=serializers.CharField(read_only=True)
    post=serializers.CharField(read_only=True)
    class Meta:
        model=comment
        exclude=("date",)

    def create(self, validated_data):
        post=self.context.get("post")
        user=self.context.get("user")
        return comment.objects.create(post=post,user=user,**validated_data)