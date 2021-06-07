from rest_framework.decorators import api_view
from ..models import Request
from rest_framework import status
from rest_framework.response import Response
from django.core import serializers


@api_view(["POST"])
def add_request(request):
    job_request = request.data
    #  create the request
    request_obj = Request.objects.create(
        description=job_request["description"],
        latitude=job_request["latitude"],
        longitude=job_request["longitude"],
        person_id=job_request["person_id"],
        mechanic_id=job_request["mechanic_id"]
    )
    response = {
        "success": "True",
        "message": "Request created successfully",
        "request": serializers.serialize('json', request_obj)
    }
    return Response(response, status=status.HTTP_200_OK)