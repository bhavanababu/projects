from django.urls import path
from bookapp import views
urlpatterns=[
    path("register",views.SignUpView.as_view(),name='register'),
path("", views.LoginView.as_view(),name="signin"),
path("home",views.IndexView.as_view(),name="Index"),
path("signout",views.SignoutView.as_view(),name="signout"),
path("books",views.BookAddView.as_view(),name="add-book"),
path("books/all", views.BookListView.as_view(), name="booklist"),

]