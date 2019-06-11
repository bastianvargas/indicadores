from rest_framework import generics
from rest_framework.permissions import AllowAny

from indicator.models import Currency
from indicator.serializers import CurrencySerializer


class CurrencyView(generics.ListCreateAPIView):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
    permission_classes = (AllowAny,)
