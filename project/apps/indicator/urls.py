from django.urls import path

from indicator.views import CurrencyView

urlpatterns = [
    path('currency/', CurrencyView.as_view())
]
