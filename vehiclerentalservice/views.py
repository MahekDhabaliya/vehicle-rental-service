from django.http import JsonResponse
from django.views import View
from .models import Vehicle
import json
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@method_decorator(csrf_exempt, name='dispatch')
class Vehicle(View):
    def get(self):
        vehicles = list(Vehicle.objects.all())
        return JsonResponse(vehicles, safe=False)
    
    def post(self, request):
        data = json.loads(request.body)
        vehicle = Vehicle.objects.create_vehicle(
            title=data['title'],
            manufactured_date = data['manufactured_date']
        )
        return JsonResponse(vehicle, status=201)