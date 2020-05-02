from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
import json
import base64
import random


# Create your views here.
@api_view(["POST"])
def image(num):
    try:
        load = json.loads(num.body)
        # result = str(load * 10)
        filename = "imageToSave"+str(random.randint(0, 1000000))+".jpg"
        fh = open(filename, "wb")
        fh.write(base64.b64decode(load))
        fh.close()
        return JsonResponse("our result is " + filename, safe=False)
    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)

# @api_view(["GET"])
# class UploadImageViewSet(viewsets.ModelViewSet):
#     queryset = UploadImage.objects.all()
#     serializer_class = UploadImageSerializer
