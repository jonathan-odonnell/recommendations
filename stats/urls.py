from django.urls import path
from . import views

urlpatterns = [
    path('', views.coffee_stats, name='coffee_stats'),
]
