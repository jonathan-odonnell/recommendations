from django.urls import path
from . import views

urlpatterns = [
    path('', views.coffee_recommendations, name='coffee_recommendations'),
    path('results/', views.coffee_recommendations_results, name='coffee_recommendations_results'),
]
