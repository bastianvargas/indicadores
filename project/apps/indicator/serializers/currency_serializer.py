from rest_framework import serializers

from indicator.models import Date


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Date
        fields = ('date_currency', 'value')
