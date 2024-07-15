from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import CryptoInvestments, SoldCrypto
from .serializers import CryptoInvestmentSerializer, SoldCryptoSerializer


class UserOwnedViewSet(viewsets.ModelViewSet):
    """
    A base viewset for models owned by a user.
    Assumes that the model has a ForeignKey to the user.
    """

    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CryptoInvestmentViewSet(UserOwnedViewSet):
    queryset = CryptoInvestments.objects.all()
    serializer_class = CryptoInvestmentSerializer


class SoldCryptoViewSet(UserOwnedViewSet):
    queryset = SoldCrypto.objects.all()
    serializer_class = SoldCryptoSerializer
