from faker import Faker
import random
import os
import django
from random import randint 
from django.conf import settings
fake = Faker()
from models import car, Maker 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'xcv_site.settings')
django.setup()



def generate_unique_car_data():
    maker = Maker.objects.get_or_create(name=fake.company())[0]
    car_name = fake.unique.word()
    hpp = random.randint(100, 500)
    launch_date = fake.date_between(start_date="-10y", end_date="today")
    
    return maker, car_name, hpp, launch_date

def create_unique_cars(num_cars):
    cars_created = 0
    
    while cars_created < num_cars:
        try:
            maker, car_name, hpp, launch_date = generate_unique_car_data()
            car.objects.create(maker=maker, car_name=car_name, hpp=hpp, launch_date=launch_date)
            cars_created += 1
        except Exception as e:
            print(e)

if __name__ == "__main__":
    num_cars_to_create = 100
    create_unique_cars(num_cars_to_create)
    print(f"Created {num_cars_to_create} unique Car objects.")