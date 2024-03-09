from django.urls import path


from lessons.views import fruits, create_fruit, detail_fruits


urlpatterns = [
    path('fruits/', fruits),
    path('fruits/<int:pk>', detail_fruits),
    path('fruits/create/', create_fruit),




]