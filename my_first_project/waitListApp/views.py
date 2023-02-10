from rest_framework import viewsets, generics

from .models import Investment
from .serializers import InvestmentSerializer
from django.http import HttpResponse, JsonResponse


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


def get_available_list(request):
    status = request.GET.get('status')
    raw_data = Investment.objects.raw(f'SELECT * FROM waitListApp_investment WHERE status = "{status}"')
    data = [{field.name: getattr(obj, field.name) for field in obj._meta.fields} for obj in raw_data]
    return JsonResponse(data, safe=False)
