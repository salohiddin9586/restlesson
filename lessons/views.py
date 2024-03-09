from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request

# from lessons.seriallizers import FruitSerializer

fruits_list = [
    {"id": 1, "name": "apple", "price": 83},
    {"id": 2, "name": "banana", "price": 57},
    {"id": 3, "name": "orange", "price": 94},
]


@api_view(http_method_names=["GET"])
def fruits(request: Request):
    return Response(fruits_list, status=200)


@api_view(http_method_names=['POST'])
def create_fruit(request: Request):
    data = request.data
    fruits_list.append(data)
    return Response(fruits_list, status=201)


@api_view(http_method_names=["GET"])
def detail_fruits(request: Request, pk: int):
    fruit = [i for i in fruits_list if i['id'] == pk]
    return Response(fruit, status=200)
