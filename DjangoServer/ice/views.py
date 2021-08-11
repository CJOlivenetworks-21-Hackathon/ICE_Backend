import json
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework import status
import os
import pymysql

image_dir = 'image경로'
user_allergy = '돼지고기'

rds_host = "localhost"
name = "root"
password = "cjon"
db_name = "ice"
conn = pymysql.connect(host=rds_host, user=name, passwd=password, db=db_name, connect_timeout=5)


@api_view(['GET', 'POST'])
def product_prediction(request):
    if request.method == 'GET':
        return HttpResponse("웹 TEST", status=status.HTTP_200_OK)
        # try:
        #     with conn.cursor() as cursor:
        #         cursor.execute("select * from product;")
        #         allergy_list = cursor.fetchall()
        # finally:
        #     conn.close()
        # return HttpResponse({"모냐": allergy_list}, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        try:
            filename = str(request.FILES['image'])
            handle_uploaded_file(request.FILES['image'], filename)
        except:
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

        image_source = image_dir + filename
        predict_result = predict_products(image_source)

        # 임시 데이터
        predict_result = [{"name": "코카콜라", "x": 100, "y": 200, "w": 50, "h": 100},
                          {"name": '스팸', "x": 200, "y": 300, "w": 100, "h": 100}]

        for product in predict_result:
            product['is_safe'] = filtering_allergy(product['name'])

        json_response = {"result": predict_result}
        os.remove(image_source)
        return JsonResponse(json_response, status=status.HTTP_200_OK)


# 임시
def predict_products(chunk):
    return 1


def handle_uploaded_file(f, filename):
    with open(image_dir + filename, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def filtering_allergy(product_name):
    # 임시
    return True

    # is_safe = True
    # try:
    #     with conn.cursor() as cursor:
    #         cursor.execute(
    #             "select name from product where allergy like '%'+product_name+'%';")
    #         allergy_list = cursor.fetchall()
    #         if allergy_list:
    #             is_safe = True
    #         else:
    #             is_safe = False
    # finally:
    #     conn.close()
    #     return is_safe
