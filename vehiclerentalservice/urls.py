# from django.urls import path
# from .views import Vehicle

# urlpatterns = [
#     path('vehicle/', Vehicle.as_view(), name='get'),
#     path('vehicle/', Vehicle.as_view(), name='post'),
# ]



# urls.py
from django.urls import path
from . import views
from .views import register_user, login_user, logout_user

# URL patterns for the vehiclerentalservice app
urlpatterns = [
    path('add/', views.add_vehicle, name='add_vehicle'),  # Add a new vehicle
    path('update/<int:vehicle_id>/', views.update_vehicle, name='update_vehicle'),  # Update a vehicle
    path('delete/<int:vehicle_id>/', views.delete_vehicle, name='delete_vehicle'),  # Delete a vehicle
    path('list/', views.list_vehicles, name='list_vehicles'),  # List all vehicles
    path('detail/<int:vehicle_id>/', views.vehicle_detail, name='vehicle_detail'),  # Get details of a specific vehicle
    path('register/', register_user, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'), 
]
