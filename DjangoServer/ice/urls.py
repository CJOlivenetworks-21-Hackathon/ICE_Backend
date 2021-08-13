from django.urls import path

from . import views

app_name = 'ice'
urlpatterns = [
    path('pr/', views.product_prediction),
]