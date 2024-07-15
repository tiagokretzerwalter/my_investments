from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register("crypto", views.CryptoInvestmentViewSet, basename="crypto")
router.register("sold-crypto", views.SoldCryptoViewSet, basename="sold-crypto")

app_name = "investments_types"

urlpatterns = [path("", include(router.urls))]
