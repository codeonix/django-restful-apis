from rest_framework import viewsets, generics
from .models import Investment
from .serializers import InvestmentSerializer


class InvestmentViewSet(viewsets.ModelViewSet):
    queryset = Investment.objects.all()
    serializer_class = InvestmentSerializer


class InvestmentUpdateAPIView(generics.UpdateAPIView):
    queryset = Investment.objects.all()
    serializer_class = InvestmentSerializer

    def perform_update(self, serializer):
        serializer.save()


class InvestmentDeleteAPIView(generics.DestroyAPIView):
    queryset = Investment.objects.all()
    serializer_class = InvestmentSerializer
