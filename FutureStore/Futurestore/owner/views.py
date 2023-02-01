from django.shortcuts import render,redirect


# Create your views here.
from  owner.models import Order

from django.views.generic import TemplateView,ListView,DetailView
from django.core.mail import send_mail
from owner.form import OrderUpdateForm



class AdminDashBoardView(TemplateView):
    template_name ="dashboard.html"

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        cnt=Order.objects.filter(status="order-placed").count()
        context["count"]=cnt
        return context


class OrderListview(ListView):
    model = Order
    context_object_name = "order"
    template_name = "admin-listorder.html"

    def get_queryset(self):
        return Order.objects.filter(status="order-placed")

class OrderDetailView(DetailView):
    model = Order
    template_name = "order-details.html"
    pk_url_kwarg = "id"
    context_object_name = "order"

    def get_context_data(self, **kwargs):
        context=super().get_context_data()
        form=OrderUpdateForm()
        context["form"]=form
        return context
    def post(self,request,*args,**kwargs):
        order=self.get_object()

        form=OrderUpdateForm(request.POST)
        if form.is_valid():
            order.status=form.cleaned_data.get("status")
            order.expected_delivery_date=form.cleaned_data.get("expected_delivery_date")
            dt=form.cleaned_data.get("expected_delivery_date")
            order.save
            send_mail(
                "order delivery update future store",
                f"your order will be delivered on{dt}",
                "bhavanakbabu2022@gmail.com",
                ["bhavanababu3510@gmail.com"]
            )
            print(form.cleaned_data)
            return redirect("dashboard")






