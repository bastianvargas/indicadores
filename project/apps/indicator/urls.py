from django.urls import path, include
from .views import CurrencyView, CurrencyDetailView, PriceView
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('', CurrencyView.as_view()),
    path('currency/<str:code>/', CurrencyDetailView.as_view()),
    path('currency/<str:code>/price', PriceView.as_view()),
    path('currency/', CurrencyView.as_view())
]
