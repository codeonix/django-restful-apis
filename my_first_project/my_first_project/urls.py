from django.contrib import admin
from django.urls import path, include

from waitListApp.views import InvestmentUpdateAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('wait-list/', include('waitListApp.urls')),

]
