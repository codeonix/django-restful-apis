from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import InvestmentViewSet, InvestmentUpdateAPIView, InvestmentDeleteAPIView, get_available_list

router = DefaultRouter()
router.register(r'investments', InvestmentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('investments/<int:id>/', InvestmentUpdateAPIView.as_view(), name='investment-update'),
    path('investments/<int:id>/', InvestmentDeleteAPIView.as_view(), name='investment-delete'),
    path('where/', get_available_list)
]
