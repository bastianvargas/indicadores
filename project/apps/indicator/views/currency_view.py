from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from indicator.models import Currency
from indicator.serializers import CurrencySerializer
from django.db.models import Q
# import requests
# from dateutil.parser import parse

# def LoadDataView(url):
#     currencies = {'uf': 1977, 'dolar': 1984, 'euro': 1999, 'bitcoin': 2009}
#     currency = Currency()
#     for c in currencies.items():
#         for r in range(c[1], 2020):
#             response = requests.get('https://{}/api/{}/{}'.format(url, c[0], r))
#             response_json = response.json()
#             for resj in response_json['serie']:
#                 currency_date=resj['fecha'][0:-14]
#                 currency_price=resj['value']
#
#                 currency.code=c[0]
#                 currency.date=currency_date
#                 carrency.value=currency_price
#                 try:
#                     currency.save()
#                 except:
#                     print("Error with save currency object: ", currency)
#     count_obj = Currency.objects.all()
#     return count_obj.count()
    # response = requests.get('https://undefined/api/{tipo_indicador}/{yyyy}')
    # pass


class PriceView(generics.ListCreateAPIView):
    serializer_class = CurrencySerializer
    permission_classes = (AllowAny,)
    def get_queryset(self, *args, **kwargs):
        queryset = Currency.objects.all()
        query = self.request.GET.get("value")
        print("queryyyyyyyy", query)
        query2 = self.request.GET.get("date")
        print("2222222", query2)
        #print("code/////", self.get_queryset())
        # if query:
        #     queryset= queryset.filter(
        #     Q(code__icontains=query)
        #     ).distinct()
        # return queryset

class CurrencyDetailView(generics.ListCreateAPIView):
    serializer_class = CurrencySerializer
    permission_classes = (AllowAny,)

    def get(self, request, code):
        currency = Currency.objects.get(code=code)
        currency_serializer = CurrencySerializer(currency)
        return Response(currency_serializer.data)

class CurrencyView(generics.ListCreateAPIView):

    serializer_class = CurrencySerializer
    permission_classes = (AllowAny,)

    def get_queryset(self, *args, **kwargs):

        queryset = Currency.objects.all()
        query = self.request.GET.get("currency")
        print("queryyyyyyyy", query)
        query2 = self.request.GET.get("code")
        print("2222222", query2)
        #print("code/////", self.get_queryset())
        if query:
            queryset= queryset.filter(
            Q(code__icontains=query)
            ).distinct()

        return queryset
