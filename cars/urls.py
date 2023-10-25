from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.based, name='members'),
    path('list/<str:suffix_string>/', views.fetch_car_data, name='list'),
    path('maker_form/', views.MakerData, name='maker'),
]