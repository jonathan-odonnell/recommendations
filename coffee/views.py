from django.shortcuts import render
from .models import CoffeeQuality
from .forms import CoffeeQualityForm
from decimal import Decimal


def coffee_recommendations(request):
    form = CoffeeQualityForm()
    template = 'coffee_recommendations.html'
    context = {'form': form}
    return render(request, template, context)


def coffee_recommendations_results(request):
    if request.method == 'POST':
        thresholds = {
            'Low': '0.00_7.33',
            'Medium': '7.34_7.66',
            'High': '7.67_10.00',
        }
        recommendations = CoffeeQuality.objects.filter(
            aroma__gte=Decimal(thresholds[request.POST['aroma']].split('_')[0]),
            aroma__lte=Decimal(thresholds[request.POST['aroma']].split('_')[1]),
            flavour__gte=Decimal(thresholds[request.POST['flavour']].split('_')[0]),
            flavour__lte=Decimal(thresholds[request.POST['flavour']].split('_')[1]),
            aftertaste__gte=Decimal(thresholds[request.POST['aftertaste']].split('_')[0]),
            aftertaste__lte=Decimal(thresholds[request.POST['aftertaste']].split('_')[1]),
            acidity__gte=Decimal(thresholds[request.POST['acidity']].split('_')[0]),
            acidity__lte=Decimal(thresholds[request.POST['acidity']].split('_')[1]),
            body__gte=Decimal(thresholds[request.POST['body']].split('_')[0]),
            body__lte=Decimal(thresholds[request.POST['body']].split('_')[1]),
            balance__gte=Decimal(thresholds[request.POST['balance']].split('_')[0]),
            balance__lte=Decimal(thresholds[request.POST['balance']].split('_')[1]),
        )[:10]
        template = 'coffee_recommendations_results.html'
        context = {'recommendations': recommendations}
        return render(request, template, context)
    else:
        recommendations = CoffeeQuality.objects.all()[:10]
        template = 'coffee_recommendations_results.html'
        context = {'recommendations': recommendations}
        return render(request, template, context)
