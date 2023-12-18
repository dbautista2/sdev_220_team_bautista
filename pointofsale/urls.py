"""
URL configuration for pointofsale project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from burgorders.views import MyDrinks
from burgorders.views import MyBuild
from burgorders.views import MyAddons
from burgorders.views import MenuOrderView
from burgorders.views import OrderDetailView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("addons/", MyAddons.as_view()),
    path("build/", MyBuild.as_view()),
    path("drinks/", MyDrinks.as_view()),
    path("menu-order/", MenuOrderView.as_view(), name="combined_view"),
    path("order-summary/<pk>", OrderDetailView.as_view(), name="order_summary"),
]


# html

# {% block content %}
# <h1>Order Summary</h1>
# <p>Order Number: {{ order.id }}</p>
# <!-- Displaying itemized order details -->
# <p>Total Price: {{ order.total_price }}</p>
# <p>Thank you for your order!</p>
# <script>
#     setTimeout(function() {
#         window.location.href = '/menu-order'; // Redirect to MenuOrderView
#     }, 5000); // Redirect after 5 seconds
# </script>
# {% endblock %}
