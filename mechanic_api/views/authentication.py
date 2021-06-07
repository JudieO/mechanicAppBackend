from rest_framework.decorators import api_view
from rest_framework import status
from django.http import JsonResponse
from ..models import Person


@api_view(["POST"])
def login(request):
    user_data = request.data
    user = Person.objects.filter(email=user_data['email']).first()
    if user:
        if user_data['password'] == user.password:
            user_name = user.username
            response = {
                "success": True,
                "message": "Successfully logged in",
                "username": user_name
            }
            return JsonResponse(response, safe=False)

    response = {
        "success": False,
        "message": "Login failed",
        "username": None
    }
    return JsonResponse(response, safe=False)


@api_view(["POST"])
def register(request):
    user_data = request.data
    user = Person.objects.create(email=user_data['email'],
                                 phone_number=user_data['phone_number'],
                                 username=user_data['user_name'],
                                 password=user_data['password']
                                 )
    # user.set_password(user_data['password'])
    response = {
        "success": True,
        "message": "Successfully registered",
        "username": user.username
    }
    return JsonResponse(response, safe=False)
