from django.apps import apps
from indicator.models import Currency
import requests
from dateutil.parser import parse



def run():
    currencies = {'uf': 1977, 'dolar': 1984, 'euro': 1999, 'bitcoin': 2009}
    currency = Currency()
    for c in currencies.items():
        for r in range(c[1], 2020):
            response = requests.get('https://mindicador.cl/api/{}/{}'.format(c[0], r))
            response_json = response.json()
            for resj in response_json['serie']:
                currency_date=resj['fecha'][0:-14]
                currency_price=resj['valor']

                currency.code=c[0]
                currency.date=currency_date
                currency.value=currency_price
                try:
                    currency.save()
                except:
                    print("Error with save currency object: ", currency)
    count_obj = Currency.objects.all()
    return count_obj.count()
