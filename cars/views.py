from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .forms import MakerForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from rest_framework.generics import RetrieveAPIView
from .models import car
from .serializers import CarSerializer


def based(r):
    return HttpResponse("My First Function !@#")


# def fetch_car_data(r,suffix_string):
#     date_today=date.today()
#     car_data=car.objects.all()
#     # car_data = car.objects.filter(
#     #     # launch_date__year__gt=2020,
#     #     car_name__istartswith='C'
#     # )
#     # car_data2 = [car.car_name + suffix_string for car in car_data]
#     print(car_data)
#     car_data_with_styles = []
#     alternate = False

#     for car in car_data:
#         car.car_name += suffix_string
#         row_style = 'blue' if alternate else 'white'  # Alternate row styles
#         car_data_with_styles.append((car, row_style))
#         alternate = not alternate

#     my_data = {'car_data_with_styles': car_data_with_styles}
#     print(car_data_with_styles)

#     # my_data={'car_data':car_data}
#     # print("Data:", car_data)
#     # print("hii 16")
#     return render(r,'carlist.html',context=my_data)


# def fetch_car_data(r,suffix_string):
#     date_today=date.today()
#     # car_data=car.objects.all()
#     car_data = car.objects.filter(
#         launch_date__year__gt=2020,
#         car_name__istartswith='C'
#     )
#     car_data_with_styles = []
#     alternate = False

#     for data in car_data:
#         car_name_with_suffix=str(data)+suffix_string
#         row_style = 'blue' if alternate else 'white'
#         car_data_with_styles.append((car_name_with_suffix, row_style))
#         alternate = not alternate
#     my_data2={'car_data':car_data}
#     my_data = {'car_data_with_styles': car_data_with_styles}
#     print(car_data_with_styles)
#     # print("Data:", car_data)
#     return render(r,'carlist.html',context=my_data)


def fetch_car_data(r, suffix_string):
    car_data = car.objects.filter(launch_date__year__gt=2020, car_name__istartswith="C")

    car_data_with_styles = []
    alternate = False

    for data in car_data:
        car_name_with_suffix = str(data) + suffix_string
        row_style = "blue" if alternate else "white"
        car_data_with_styles.append((car_name_with_suffix, row_style))
        alternate = not alternate

    # Create the contexts
    context = {
        "car_data": car_data,
        "car_data_with_styles": car_data_with_styles,
    }

    return render(r, "carlist.html", context=context)


def MakerData(r):
    form = MakerForm()
    if r.method == "POST":
        form = MakerForm(r.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect("https://www.google.com/")
    Make_form = {"Make_form": form}
    return render(r, "MakerForm.html", context=Make_form)


class CarListView(ListView):
    model = car
    template_name = "carlist2.html"
    context_object_name = "cars"


class CarDetailView(RetrieveAPIView):
    queryset = car.objects.all()
    serializer_class = CarSerializer
    lookup_field = "car_name"


class Carlist(APIView):
    def get(self, request):
        print("124 hii")
        data = car.objects.all()
        print(data)
        serilizer = CarSerializer(data, many=True)
        return Response(serilizer.data)

    def post(self, request):
        serializer = CarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class carupdatedelete(APIView):
    def put(self, r, pk):
        car_details = car.objects.get(id=pk)
        serializer = CarSerializer(car_details, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, r, pk):
        car_object = car.objects.get(id=pk)
        car_object.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
