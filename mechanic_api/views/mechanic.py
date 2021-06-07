from rest_framework.decorators import api_view
from ..models import Mechanic
from rest_framework import status
from django.http import JsonResponse

@api_view(["POST"])
def add_mechanic(request):
    mechanic = request.data
    #  create the request
    mechanic = Mechanic.objects.create(
        first_name=mechanic['first_name'],
        last_name=mechanic['last_name'],
        phone_number=mechanic['phone_number'],
        email=mechanic['email'],
        latitude=mechanic['latitude'],
        longitude=mechanic['longitude']
    )
    mechanic_dict = {
        "first_name": mechanic.first_name,
        "last_name": mechanic.last_name,
        "phone_number": mechanic.phone_number,
        "email": mechanic.email,
        "latitude": mechanic.latitude,
        "longitude": mechanic.longitude
    }
    response = {
        "success": "True",
        "message": "Mechanic created successfully",
        "mechanic": mechanic_dict
    }
    return JsonResponse(response, safe=False)

@api_view(["GET"])
def get_mechanics(request):
    data = request.data
    latitude = data["latitude"]
    longitude = data["longitude"]
    mechanics = list(Mechanic.objects.all().values())
    return JsonResponse({'mechanics': mechanics}, safe=False)
