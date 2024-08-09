from rest_framework.test import APITestCase, APIClient
from django.urls import reverse
from rest_framework import status
from django.contrib.auth import get_user_model
from knox.models import AuthToken
from ..models import CryptoInvestments, SoldCrypto


User = get_user_model()


class CryptoInvestmentsViewSetTest(APITestCase):
    """Test module for Crypto investments API"""

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            email="testuser@user.com", password="Testpass123."
        )
        self.token = AuthToken.objects.create(user=self.user)[1]
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token)
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

    def test_list_crypto_investments(self):
        url = reverse("investments_types:crypto-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["coin_name"], "Bitcoin")

    def test_create_crypto_investment(self):
        url = reverse("investments_types:crypto-list")
        data = {
            "coin_name": "Ethereum",
            "coin_code": "ETH",
            "amount_bought": 2.0,
            "date_invested": "2024-02-01",
            "current_price_usdt": 1800.00000,
            "price_when_bought_usdt": 1400.00000,
            "price_when_bought_real": 7000.00000,
            "original_currency": "USD",
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(CryptoInvestments.objects.count(), 2)
        self.assertEqual(
            CryptoInvestments.objects.get(id=response.data["id"]).coin_name, "Ethereum"
        )


class SoldCryptoViewSetTest(APITestCase):
    """Test module for Sold Crypto API"""

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            email="testuser@user.com", password="Testpass123."
        )
        self.token = AuthToken.objects.create(user=self.user)[1]
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token)
        self.sold_crypto = SoldCrypto.objects.create(
            user=self.user,
            coin_name="Ethereum",
            amount_sold=2.0,
            date_sold="2024-02-01",
            destined_currency="USD",
            price_when_sold_real=1800.00000,
            price_when_sold_usdt=1800.00000,
        )

    def test_list_sold_crypto(self):
        url = reverse("investments_types:sold-crypto-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["coin_name"], "Ethereum")

    def test_create_sold_crypto(self):
        url = reverse("investments_types:sold-crypto-list")
        data = {
            "coin_name": "Bitcoin",
            "amount_sold": 1.0,
            "date_sold": "2024-03-01",
            "destined_currency": "USD",
            "price_when_sold_real": 2000.00000,
            "price_when_sold_usdt": 2000.00000,
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(SoldCrypto.objects.count(), 2)
        self.assertEqual(
            SoldCrypto.objects.get(id=response.data["id"]).coin_name, "Bitcoin"
        )
