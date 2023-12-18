from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.views.generic import FormView, DetailView

from .models import Burger, Drink, Side, Topping, Sauce, Order

from .forms import OrderForm

from django.views.generic import DetailView


class OrderDetailView(DetailView):
    template_name = "burgorders/order_summary.html"
    model = Order

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["order"] = self.object
        return context


class MenuView(View):
    template_name = "burgorders/menu.html"

    def get(self, request):
        burgers = Burger.objects.filter(is_signature=True)
        drinks = Drink.objects.all()
        sides = Side.objects.all()
        toppings = Topping.objects.all()

        context = {
            "burgers": burgers,
            "drinks": drinks,
            "sides": sides,
            "toppings": toppings,
        }

        return render(request, self.template_name, context)


class MyAddons(View):
    template_name = "burgorders/addons.html"

    def get(self, request):
        signature = Burger.objects.filter(is_signature=True)
        context = {"burgers": signature}
        return render(request, self.template_name, context)


class MyBuild(View):
    template_name = "burgorders/build.html"

    def get(self, request):
        signature = Burger.objects.filter(is_signature=True)
        context = {"burgers": signature}
        return render(request, self.template_name, context)


class MyDrinks(View):
    template_name = "burgorders/drinks.html"

    def get(self, request):
        drinks = Drink.objects.all()  # Retrieve all drinks
        context = {"drinks": drinks}
        return render(request, self.template_name, context)


# class MySides(View):
#     template_name = "burgorders/sides.html"
#     def get(self, request):
#         signature = Burger.objects.filter(is_signature=True)
#         context = {'burgers': signature}
#         return render(request, self.template_name, context)
#
#
# class MySignature(View):
#     template_name = "burgorders/signature.html"
#     def get(self, request):
#         signature = Burger.objects.filter(is_signature=True)
#         context = {'burgers': signature}
#         return render(request, self.template_name, context)
#
#
# class MyToppings(View):
#     template_name = "burgorders/toppings.html"
#     def get(self, request):
#         signature = Burger.objects.filter(is_signature=True)
#         context = {'burgers': signature}
#         return render(request, self.template_name, context)
#
#
# class MySauce(View):
#     template_name = "burgorders/sauces.html"
#     def get(self, request):
#         signature = Burger.objects.filter(is_signature=True)
#         context = {'burgers': signature}
#         return render(request, self.template_name, context)


class MenuOrderView(FormView):
    template_name = "burgorders/menu.html"

    def get_context_data(self, **kwargs):
        burgers = Burger.objects.filter(is_signature=True)
        drinks = Drink.objects.all()
        sides = Side.objects.all()
        sauces = Sauce.objects.all()
        context = {
            "burgers": burgers,
            "drinks": drinks,
            "sides": sides,
            "sauces": sauces,
            "order_form": OrderForm(),
        }
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        context["form"] = OrderForm()
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = OrderForm(request.POST)
        if form.is_valid():
            # Logic to create an Order instance and save it
            order = Order()
            order.save()
            order.burgers.set(form.cleaned_data['burgers'])
            order.sides.set(form.cleaned_data['sides'])
            order.drinks.set(form.cleaned_data['drinks'])
            order.sauces.set(form.cleaned_data['sauces'])
            return redirect("order_summary", pk=order.id)
        else:
            return render(request, self.template_name, {"order_form": form})

