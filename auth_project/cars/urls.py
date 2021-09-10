from django.urls import path
from cars import views

urlpatterns = [
    path('', views.get_cars)
]
