from django.urls import path
from . import views

urlpatterns = [
    path('nutrients/', views.coffee_nutrients_stats, name='coffee_nutrients_stats'),
    path('sales/', views.coffee_sales_stats, name='coffee_sales_stats'),
]
