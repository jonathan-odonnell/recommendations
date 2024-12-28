from django.shortcuts import render
import pandas as pd


def coffee_stats(request):
    df = pd.read_csv('stats/fixtures/starbucks.csv')
    beverages_value_count = df['Beverage_category'].value_counts()
    nutrients = df.groupby('Beverage_category')['Calories'].mean().nlargest()
    nutrients = nutrients.reset_index()
    categories = list(df.columns)[3:]
    current_category = 'Calories'

    if request.GET and 'category' in request.GET:
        current_category = request.GET['category']

    dataset = {
        'beverage_labels': beverages_value_count.index.to_list(),
        'beverage_data': beverages_value_count.to_list(),
        'nutrients_labels': nutrients['Beverage_category'].to_list(),
        'nutrients_data': nutrients['Calories'].to_list()
    }
    template = 'stats.html'
    context = {
        'dataset': dataset,
        'current_category': current_category,
        'categories': categories,
        'count': df.count()['Beverage'],
        'min': df['Calories'].min(),
        'max': df['Calories'].max(),
        'average': df['Calories'].mean(),
        }
    return render(request, template, context)
