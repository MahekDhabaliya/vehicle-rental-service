from django.urls import path
from . import views

urlpatterns = [
    path('', views.DisputeListCreateView.as_view(), name='dispute-list'),
]