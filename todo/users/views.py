from rest_framework import generics

from users.models import SchemeData
from .serializers import SchemeDataSerializer


class SchemeDataList(generics.ListAPIView):
    queryset = SchemeData.objects.all()
    serializer_class = SchemeDataSerializer


class SchemeDataDetail(generics.ListAPIView):
    queryset = SchemeData.objects.all()
    serializer_class = SchemeDataSerializer
    lookup_field = 'scheme_uid'

    def get_queryset(self):
        scheme_uid = self.kwargs.get('scheme_uid', None)
        return self.queryset.filter(scheme_uid=scheme_uid)


