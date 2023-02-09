from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets

from tasks.models import SchemeModel
from tasks.serializers import SchemeSerializer


def all_todo(request):
    return HttpResponse('All the tasks are listed here')


class SchemeViewSet(viewsets.ModelViewSet):
    queryset = SchemeModel.objects.all()
    serializer_class = SchemeSerializer
