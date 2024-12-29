from django.shortcuts import render
import pandas as pd
from .models import Nutrient, Stat 
from decimal import Decimal


def coffee_stats(request):
    current_category = 'calories'

    if request.GET and 'category' in request.GET:
        current_category = request.GET['category']

    df = pd.DataFrame(list(Stat.objects.all().values()))
    beverages_value_count = df['category'].value_counts()
    nutrients = df.groupby('category')[current_category].mean()
    nutrients = nutrients.reset_index()
    categories = Nutrient.objects.order_by('id')
    category = Nutrient.objects.get(name__iexact=current_category.replace('_', ' '))

    dataset = {
        'category': category.name,
        'unit': category.units,
        'beverage_labels': beverages_value_count.index.to_list(),
        'beverage_data': beverages_value_count.to_list(),
        'nutrients_labels': nutrients['category'].to_list(),
        'nutrients_data': nutrients[current_category].to_list()
    }
    template = 'stats.html'
    context = {
        'dataset': dataset,
        'current_category': category,
        'categories': categories,
        'count': df.count()['name'],
        'min': df[current_category].min(),
        'max': df[current_category].max(),
        'average': df[current_category].mean(),
        }
    return render(request, template, context)
