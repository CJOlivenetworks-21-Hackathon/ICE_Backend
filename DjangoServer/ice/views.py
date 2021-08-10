import json
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework import status
import os

image_dir = 'image경로'


@api_view(['GET', 'POST'])
def product_prediction(request):
    if request.method == 'GET':
        return HttpResponse("웹 TEST", status=status.HTTP_200_OK)
    elif request.method == 'POST':
        try:
            filename = str(request.FILES['image'])
            handle_uploaded_file(request.FILES['image'], filename)
        except:
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

        image_source = image_dir + filename
        predict_result = predict_product(image_source)

        json_response = {"result": predict_result}
        os.remove(image_source)
        return JsonResponse(json_response, status=status.HTTP_200_OK)


# 임시
def predict_product(chunk):
    return 1


def handle_uploaded_file(f, filename):
    with open(image_dir + filename, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
