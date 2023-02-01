from django.shortcuts import render,redirect
from django.views.generic import View,ListView,CreateView,UpdateView,DetailView,TemplateView
from bookapp import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from bookapp.models import Book
from django.urls import reverse_lazy
from django.contrib import messages



class SignUpView(CreateView):
    model = Book
    form_class = forms.RegistrationForm
    template_name = "registration.html"
    success_url = reverse_lazy("signin")

    def form_valid(self, form):
        messages.success(self.request, "regiatration succesfully")
        return super().form_valid(form)
    # def get(self,request,*args,**kwargs):
    #     form=forms.RegistrationForm()
    #     return render(request,"registration.html",{"form":form})
    #
    # def post(self,request,*args,**kwargs):
    #     form =forms.RegistrationForm(request.POST)
    #     if form.is_valid():
    #
    #         User.objects.create_user(**form.cleaned_data)
    #         return redirect("signin")
    #     else:
    #         return render(request, "registrations.html",{"form": form})


class LoginView(View):
    def get(self,request,*args,**kwargs):
        form=forms.Loginform()
        return render(request,"login.html",{"form":form})

    def post(self,request,*args,**kwargs):
        form=forms.Loginform(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            user=authenticate(request,username=uname,password=pwd)
            if user:
                login (request,user)
                print("login success")
                return redirect("Index")
            else:
                print("invalid credientials")
        return render(request, "login.html", {"form": form})


class IndexView(TemplateView):
    template_name = "home.html"
    # def get(self,request,*args,**kwargs):
    #     return render(request,"home.html")

class SignoutView(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect("signin")



class BookAddView(CreateView):
    model = Book
    form_class = forms.BookForm
    template_name = "add-book.html"
    success_url = reverse_lazy("booklist")

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "book has been added")
        return super().form_valid(form)
    # def get(self,request,*args,**kwargs):
    #     form=forms.BookForm()
    #     return render(request,"add-book.html",{"form":form})
    # def post(self,request,*args,**kwargs):
    #     form=forms.BookForm(request.POST)
    #     if form.is_valid():
    #         form.instance.user=request.user
    #         form.save()
    #         return redirect("Index")
    #     else:
    #         return render(request, "add-book.html", {"form": form})

class BookListView(ListView):
    model = Book
    context_object_name = "books"
    template_name = "booklist.html"

    def get_queryset(self):
        return Book.objects.filter(user=self.request.user)
    # def get(self,request,*args,**kwargs):
    #     all_books=Book.objects.all()
    #     return render(request,"booklist.html",{"books":all_books})

