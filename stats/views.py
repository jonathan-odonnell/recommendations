from django.shortcuts import render

def coffee_stats(request):
    template = 'stats.html'
    return render(request, template)
