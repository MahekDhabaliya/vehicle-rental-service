from django.urls import path
from .views import Vehicle

urlpatterns = [
    path('vehicle/', Vehicle.as_view(), name='get'),
    path('vehicle/', Vehicle.as_view(), name='post'),
]
