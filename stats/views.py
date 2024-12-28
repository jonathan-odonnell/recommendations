from django.shortcuts import render
import pandas as pd


def coffee_stats(request):
    current_category = 'Calories'

    if request.GET and 'category' in request.GET:
        current_category = request.GET['category']

    df = pd.read_csv('stats/fixtures/starbucks.csv')

    if pd.api.types.is_string_dtype(df.dtypes[current_category]):
        df[current_category] = df[current_category].str.replace("%", '').astype(float)

    beverages_value_count = df['Beverage_category'].value_counts()
    nutrients = df.groupby('Beverage_category')[current_category].mean().nlargest()
    nutrients = nutrients.reset_index()
    categories = list(df.columns)[3:]

    dataset = {
        'category': current_category,
        'beverage_labels': beverages_value_count.index.to_list(),
        'beverage_data': beverages_value_count.to_list(),
        'nutrients_labels': nutrients['Beverage_category'].to_list(),
        'nutrients_data': nutrients[current_category].to_list()
    }
    template = 'stats.html'
    context = {
        'dataset': dataset,
        'current_category': current_category,
        'categories': categories,
        'count': df.count()['Beverage'],
        'min': df[current_category].min(),
        'max': df[current_category].max(),
        'average': df[current_category].mean(),
        }
    return render(request, template, context)
