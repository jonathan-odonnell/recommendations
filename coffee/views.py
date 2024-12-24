from django.shortcuts import render


def coffee_recommendations(request):
    if request.GET:
        template = 'coffee_recommendations.html'
        return render(request, template)


def coffee_recommendations_results(request):
    template='coffee_recommendations_results.html'
    return render(request, template)