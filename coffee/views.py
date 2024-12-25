from django.shortcuts import render
from .models import CoffeeQuality
from .forms import CoffeeQualityForm


def coffee_recommendations(request):
    if request.method == 'POST':
        return
    else:
        form = CoffeeQualityForm()
        template = 'coffee_recommendations.html'
        context = {'form': form}
        return render(request, template, context)


def coffee_recommendations_results(request):
    recommendations = CoffeeQuality.objects.all()[:10]
    template='coffee_recommendations_results.html'
    context = {'recommendations': recommendations}
    return render(request, template, context)