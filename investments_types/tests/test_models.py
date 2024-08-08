from django.test import TestCase
from django.contrib.auth import get_user_model
from ..models import CryptoInvestments, SoldCrypto


User = get_user_model()


class CryptoInvestmentsTest(TestCase):
    """Test module for CryptoInvestments model"""

    def setUp(self):
        self.user = User.objects.create_user(
            email="testuser@gmail.com", password="12345", name="testuser"
        )
        self.investment = CryptoInvestments.objects.create(
            user=self.user,
            coin_name="Bitcoin",
            coin_code="BTC",
            amount_bought=1.5,
            date_invested="2024-01-01",
            current_price_usdt=30000.00000,
            price_when_bought_usdt=15000.00000,
            price_when_bought_real=78000.00000,
            original_currency="USD",
        )

    def test_crypto_investment_creation(self):
        self.assertEqual(self.investment.coin_name, "Bitcoin")
        self.assertEqual(self.investment.user.email, "testuser@gmail.com")
        self.assertEqual(self.investment.amount_bought, 1.5)
        self.assertEqual(str(self.investment), "testuser's Investment in BTC")


class SoldCryptoModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email="testuser@gmail.com", password="12345", name="testuser"
        )
        self.sold_crypto = SoldCrypto.objects.create(
            user=self.user,
            coin_name="Ethereum",
            amount_sold=2.0,
            date_sold="2024-02-01",
            destined_currency="USD",
            price_when_sold_real=1800.00000,
            price_when_sold_usdt=1800.00000,
        )

    def test_sold_crypto_creation(self):
        self.assertEqual(self.sold_crypto.coin_name, "Ethereum")
        self.assertEqual(self.sold_crypto.user.email, "testuser@gmail.com")
        self.assertEqual(self.sold_crypto.amount_sold, 2.0)
        self.assertEqual(str(self.sold_crypto), "testuser's Sale of Ethereum")
