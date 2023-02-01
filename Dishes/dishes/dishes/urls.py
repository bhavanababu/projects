"""dishes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from disheitem.views import DishesView,DishesDetailsview,DishDetailModelView,Dishemodelview,Disheviewsetview
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register("api/v3/dishes",Disheviewsetview,basename="dishes")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dishitem/dishes/',DishesView.as_view()),
    path('myg/dishes/<int:id>',DishesDetailsview.as_view()),
    path('api/v2/myg/dishes',Dishemodelview.as_view()),
    path('api/v2/myg/dishes/<int:id>',DishDetailModelView.as_view())
]+router.urls

