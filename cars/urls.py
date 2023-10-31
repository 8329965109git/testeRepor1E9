from django.urls import path
from . import views
from .views import CarDetailView, Carlist, carupdatedelete


urlpatterns = [
    path("test/", views.based, name="members"),
    path("list/<str:suffix_string>/", views.fetch_car_data, name="list"),
    path("maker_form/", views.MakerData, name="maker"),
    path("carlist", views.CarListView.as_view(), name="carlist"),
    path("<str:car_name>/", CarDetailView.as_view(), name="car-detail"),
    path("car_details/", Carlist.as_view()),
    path("car_update/<pk>", carupdatedelete.as_view()),
]
