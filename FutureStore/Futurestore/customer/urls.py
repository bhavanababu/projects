from django.urls import path
from customer import views

urlpatterns = [
    path('register', views.RegistrationView.as_view(), name="register"),
    path("", views.LoginView.as_view(), name="login"),
    path("home", views.HomeView.as_view(), name="home"),
    path("logout", views.LogoutView.as_view(), name="logout"),
    path("product/<int:id>", views.ProductDetailView.as_view(), name="product-detail"),
    path("product/<int:id>/carts/add",views.Addcart.as_view(),name="add-cart"),
    path("carts/all",views.MycartView.as_view(),name="mycart"),
    path("carts/remove/<int:id>",views.CartRemoveView.as_view(),name="cart-remove"),
    path("carts/placeorder/<int:cid>/<int:pid>",views.PlaceOrderView.as_view(),name="place-order"),
    ]