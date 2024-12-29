from django.shortcuts import render
import pandas as pd
from .models import Nutrient, Stat


def coffee_stats(request):
    current_category = 'calories'

    if request.GET and 'category' in request.GET:
        current_category = request.GET['category']

    df = pd.DataFrame(list(Stat.objects.all().values()))
    beverage_categories_value_count = df['category'].value_counts()
    beverages_value_count = pd.concat([df['name'].value_counts().head(5), df['name'].value_counts().tail(5)]).sort_index()
    nutrients = df.groupby('category')[current_category].mean()
    nutrients = nutrients.reset_index()
    categories = Nutrient.objects.order_by('id')
    category = Nutrient.objects.get(name__iexact=current_category.replace('_', ' '))

    dataset = {
        'category': category.name,
        'unit': category.units,
        'beverage_categories_labels': beverage_categories_value_count.index.to_list(),
        'beverages_data': beverages_value_count.to_list(),
        'beverages_labels': beverages_value_count.index.to_list(),
        'beverage_categories_data': beverage_categories_value_count.to_list(),
        'nutrients_labels': nutrients['category'].to_list(),
        'nutrients_data': nutrients[current_category].to_list(),
        'calories_sugar_labels': df['sugar'].to_list(),
        'calories_sugar_data': df['calories'].to_list(),
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
