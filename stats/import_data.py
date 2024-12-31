import pandas as pd
from datetime import date, time, datetime
from .models import Sales
from decimal import Decimal

def import_data():
    Sales.objects.all().delete()
    df = pd.read_csv('stats/fixtures/coffee_shop_sales.csv')
    df = df.rename(columns={
        'transaction_id': 'id',
        'transaction_date': 'date',
        'transaction_time': 'time',
        'transaction_qty': 'quantity'
    })

    for index, row in df.head(5000).iterrows():
        s = Sales.objects.create(
            date = datetime.strptime(row['date'], "%m/%d/%y").date(),
            time = datetime.strptime(row['time'], "%H:%M:%S").time(),
            store_id = row['store_id'],
            store_location = row['store_location'],	
            product_id = row['product_id'],	
            unit_price = Decimal(row['unit_price']),
            product_category = row['product_category'],
            product_type = row['product_type'],
            product_detail = row['product_detail'],
        )
        s.save()

    qs = Sales.objects.all()
    return qs

