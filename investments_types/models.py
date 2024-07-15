from django.db import models
from django.conf import settings


class CryptoInvestments(models.Model):
    """Investment made in an specific crypto coin"""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="crypto_investments",
    )
    coin_name = models.CharField(max_length=100)
    coin_code = models.CharField(max_length=30)
    amount_bought = models.DecimalField(max_digits=20, decimal_places=5)
    date_invested = models.DateField()
    current_price_usdt = models.DecimalField(max_digits=20, decimal_places=10)
    price_when_bought_usdt = models.DecimalField(max_digits=20, decimal_places=10)
    price_when_bought_real = models.DecimalField(max_digits=20, decimal_places=10)
    original_currency = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.user.name}'s Investment in {self.coin_code}"


class SoldCrypto(models.Model):
    """Operation to sell a coin"""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="sold_coins"
    )
    coin_name = models.CharField(max_length=100)
    amount_sold = models.DecimalField(max_digits=20, decimal_places=8)
    date_sold = models.DateField()
    dentined_currency = models.CharField(max_length=30)
    price_when_sold_real = models.DecimalField(max_digits=20, decimal_places=10)
    price_when_sold_usdt = models.DecimalField(max_digits=20, decimal_places=10)

    def __str__(self):
        return f"{self.user.name}'s Sale of {self.coin_name}"
