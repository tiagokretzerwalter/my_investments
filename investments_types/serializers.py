from rest_framework import serializers
from .models import CryptoInvestments, SoldCrypto


class CryptoInvestmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CryptoInvestments
        fields = (
            "id",
            "coin_name",
            "coin_code",
            "amount_bought",
            "date_invested",
            "current_price_usdt",
            "price_when_bought_usdt",
            "price_when_bought_real",
            "original_currency",
        )
        read_only_fields = ('id',)


class SoldCryptoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SoldCrypto
        fields = (
            "id",
            "coin_name",
            "amount_sold",
            "date_sold",
            "destined_currency",
            "price_when_sold_usdt",
            "price_when_sold_real",            
        )
        read_only_fields = ('id',)
