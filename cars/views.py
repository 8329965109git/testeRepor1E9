from django.shortcuts import render
from datetime import date
from django.http import HttpResponse,HttpResponseRedirect
from .models import car
# Create your views here.
from .forms import MakerForm

def based(r):
    # request is handled using HttpResponse object
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
    date_today = date.today()
    
    # Filter cars
    car_data = car.objects.filter(
        launch_date__year__gt=2020,
        car_name__istartswith='C'
    )
    
    car_data_with_styles = []
    alternate = False

    for data in car_data:
        car_name_with_suffix = str(data) + suffix_string
        row_style = 'blue' if alternate else 'white'
        car_data_with_styles.append((car_name_with_suffix, row_style))
        alternate = not alternate

    # Create the contexts
    context = {
        'car_data': car_data,
        'car_data_with_styles': car_data_with_styles,
    }

    return render(r, 'carlist.html', context=context)



def MakerData(r):
    form = MakerForm()
    if r.method=="POST":
        form=MakerForm(r.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('https://www.google.com/')
    Make_form={'Make_form':form}
    return render(r,'MakerForm.html',context=Make_form)