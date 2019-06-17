from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from indicator.models import Currency
from indicator.serializers import CurrencySerializer
from django.db.models import Q


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
