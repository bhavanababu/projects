from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    ProfilePic=models.ImageField(upload_to="profilepics")
    DOB=models.DateField(null=True)
    gender=models.CharField(max_length=20)
    address=models.CharField(max_length=120)
    bio=models.CharField(max_length=120)
    cover_pic=models.ImageField(upload_to="profilepictures",null=True)
class Posts(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name="post")
    title=models.CharField(max_length=200)
    content=models.CharField(max_length=120)
    image=models.ImageField(upload_to="postpics",null=True)
    current_date=models.DateField(auto_now_add=True)
    liked_by=models.ManyToManyField(User)
class comment(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    post=models.ForeignKey(Posts,on_delete=models.CASCADE)
    comment=models.CharField(max_length=120)
    date=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.comment
    