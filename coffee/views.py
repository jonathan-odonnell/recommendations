from django.shortcuts import render
from .models import CoffeeQuality


def coffee_recommendations(request):
    if request.method == 'POST':
        return
    else:
        template = 'coffee_recommendations.html'
        return render(request, template)


def coffee_recommendations_results(request):
    recommendations = CoffeeQuality.objects.all()[:10]
    template='coffee_recommendations_results.html'
    context = {'recommendations': recommendations}
    return render(request, template, context)