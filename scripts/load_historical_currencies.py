from django.apps import apps
from indicator.models import Currency, Date
import requests
from dateutil.parser import parse



def run():
    currencies = {'uf': 1977, 'dolar': 1984, 'euro': 1999, 'bitcoin': 2009}
    currency = Currency()
    datec = Date()
    for c in currencies.items():
        currency.code = c[0]
        try:
            currency.save()
        except:
            print("Error with save currency object: ", currency)
        code_date=Currency.objects.get(code=c[0])
        for r in range(c[1], 2020):
            response = requests.get('https://mindicador.cl/api/{}/{}'.format(c[0], r))
            response_json = response.json()
            for resj in response_json['serie']:
                currency_date=parse(resj['fecha'][0:-14])
                currency_price=resj['valor']

                datec.code=code_date.id
                datec.date_currency=currency_date
                datec.value=currency_price
                print(datec.code)
                print(type(currency_date))
                print(datec.date_currency)
                print(datec.value)
                try:
                    datec.save()
                except:
                    print("Error with save date object: ", datec)
    count_obj = Date.objects.all()
    return count_obj.count()
