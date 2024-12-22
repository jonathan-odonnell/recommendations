from django.shortcuts import render

def coffee_recommendations(request):
    template = 'coffee_recommendations.html'
    return render(request, template)
