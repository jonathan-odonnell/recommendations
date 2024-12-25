from django.shortcuts import render
from .models import CoffeeQuality
from .forms import CoffeeQualityForm


def coffee_recommendations(request):
    form = CoffeeQualityForm()
    template = 'coffee_recommendations.html'
    context = {'form': form}
    return render(request, template, context)


def coffee_recommendations_results(request):
    if request.method == 'POST':
        thresholds = {
            'Low': '0.00_3.33',
            'Medium': '3.34_6.66',
            'High': '6.67_10.00',
        }
        recommendations = CoffeeQuality.objects.filter(
            species=request.POST['species'],
            country=request.POST['country'],
            year=int(request.POST['species']),
            variety=request.POST['colour'],
            colour=request.POST['colour'],
            processing_method=request.POST['processing_method'],
            aroma=thresholds[request.post['aroma']],
            flavour=thresholds[request.POST['flavour']],
            aftertaste=thresholds[request.POST['aftertaste']],
            acidity=thresholds[request.POST['acidity']],
            body=thresholds[request.POST['body']],
            balance=thresholds[request.POST['balance']],
            uniformity=thresholds[request.POST['uniformity']],
            sweetness=thresholds[request.POST['sweetness']],
            moisture=thresholds[request.POST['moisture']],
        )[:10]
        template = 'coffee_recommendations_results.html'
        context = {'recommendations': recommendations}
        return render(request, template, context)
    else:
        recommendations = CoffeeQuality.objects.all()[:10]
        template = 'coffee_recommendations_results.html'
        context = {'recommendations': recommendations}
        return render(request, template, context)
