# from django.http import JsonResponse
# from django.views import View
# from .models import Vehicle
# import json
# from django.utils.decorators import method_decorator
# from django.views.decorators.csrf import csrf_exempt

# # Create your views here.
# @method_decorator(csrf_exempt, name='dispatch')
# class Vehicle(View):
#     def get(self):
#         vehicles = list(Vehicle.objects.all())
#         return JsonResponse(vehicles, safe=False)
    
#     def post(self, request):
#         data = json.loads(request.body)
#         vehicle = Vehicle.objects.create_vehicle(
#             title=data['title'],
#             manufactured_date = data['manufactured_date']
#         )
#         return JsonResponse(vehicle, status=201)

from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Vehicle  # Import the Vehicle model
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import authentication_classes, permission_classes
import json

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])

# User Registration API
@csrf_exempt
@api_view(['POST'])
def register_user(request):
    data = json.loads(request.body)
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return Response({'error': 'Username and password are required'}, status=400)

    if User.objects.filter(username=username).exists():
        return Response({'error': 'Username already taken'}, status=400)

    user = User.objects.create_user(username=username, password=password)
    token, _ = Token.objects.get_or_create(user=user)

    return Response({'message': 'User registered successfully', 'token': token.key}, status=201)

# User Login API
@csrf_exempt
@api_view(['POST'])
def login_user(request):
    data = json.loads(request.body)
    username = data.get('username')
    password = data.get('password')

    user = authenticate(username=username, password=password)
    if user is None:
        return Response({'error': 'Invalid username or password'}, status=400)

    token, _ = Token.objects.get_or_create(user=user)
    return Response({'message': 'Login successful', 'token': token.key}, status=200)

# User Logout API (Token-based)
@csrf_exempt
@api_view(['POST'])
def logout_user(request):
    request.auth.delete()  # Delete the user's token
    return Response({'message': 'Logged out successfully'}, status=200)

# Add a new vehicle to the database
@csrf_exempt
def add_vehicle(request):
    if request.method == 'POST':  # Check if the request method is POST
        data = json.loads(request.body)  # Parse JSON data from the request body
        if float(data['rent_per_day']) <= 0:
            return JsonResponse({'message': 'Vehicle rent amount is invalid!!'}, status=400)

        elif str(data['type']).lower() not in ['bike', 'car']:

            return JsonResponse({'message': 'Vehicle type is invalid!!'}, status=400)


        # Create a new vehicle object and save it to the database
        vehicle = Vehicle.objects.create(
            name=data['name'],
            type=data['type'],
            rent_per_day=data['rent_per_day'],
            available=data['available']
        )
        # Return a JSON response with success message and the new vehicle's ID
        return JsonResponse({'message': 'Vehicle added successfully!', 'vehicle_id': vehicle.id}, status=201)

# Update an existing vehicle's details
@csrf_exempt
def update_vehicle(request, vehicle_id):
    if request.method == 'PUT':  # Check if the request method is PUT
        data = json.loads(request.body)  # Parse JSON data from the request body
        try:
            # Get the vehicle by ID, or raise a DoesNotExist exception
            vehicle = Vehicle.objects.get(id=vehicle_id)
            # Update the vehicle's details
            vehicle.name = data['name']
            vehicle.type = data['type']
            vehicle.rent_per_day = data['rent_per_day']
            vehicle.available = data['available']
            vehicle.save()  # Save the updated vehicle object to the database
            # Return a JSON response with a success message
            return JsonResponse({'message': 'Vehicle updated successfully!'}, status=200)
        except Vehicle.DoesNotExist:
            # If the vehicle is not found, return an error response
            return JsonResponse({'error': 'Vehicle not found!'}, status=404)

# Delete an existing vehicle
@csrf_exempt
def delete_vehicle(request, vehicle_id):
    if request.method == 'DELETE':  # Check if the request method is DELETE
        try:
            # Get the vehicle by ID, or raise a DoesNotExist exception
            vehicle = Vehicle.objects.get(id=vehicle_id)
            vehicle.delete()  # Delete the vehicle from the database
            # Return a JSON response with a success message
            return JsonResponse({'message': 'Vehicle deleted successfully!'}, status=200)
        except Vehicle.DoesNotExist:
            # If the vehicle is not found, return an error response
            return JsonResponse({'error': 'Vehicle not found!'}, status=404)

# Get a list of all vehicles
def list_vehicles(request):
    if request.method == 'GET':  # Check if the request method is GET
        # Fetch all vehicles from the database and convert them to a list of dictionaries
        vehicles = list(Vehicle.objects.values())
        # Return a JSON response with the list of vehicles
        return JsonResponse({'vehicles': vehicles}, status=200)

# Get details of a specific vehicle by ID
def vehicle_detail(request, vehicle_id):
    if request.method == 'GET':  # Check if the request method is GET
        # Fetch the vehicle by ID, or return a 404 response if not found
        vehicle = get_object_or_404(Vehicle, id=vehicle_id)
        # Create a dictionary with the vehicle's details
        vehicle_data = {
            'id': vehicle.id,
            'name': vehicle.name,
            'type': vehicle.type,
            'rent_per_day': str(vehicle.rent_per_day),  # Convert Decimal to string for JSON
            'available': vehicle.available
        }
        # Return a JSON response with the vehicle's details
        return JsonResponse({'vehicle': vehicle_data}, status=200)
