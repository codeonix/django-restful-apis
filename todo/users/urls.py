from django.urls import path, include
from .views import SchemeDataList, SchemeDataDetail

urlpatterns = [
    path('', SchemeDataList.as_view(), name='scheme-data-list'),
    path('<int:scheme_uid>', SchemeDataDetail.as_view(), name='scheme-data-detail'),
]
