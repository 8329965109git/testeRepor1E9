from django.core.management.base import BaseCommand
from faker import Faker
import random
from cars.models import car, Maker

fake = Faker()


class Command(BaseCommand):
    help = "Creates dummy data for the Car model"

    def handle(self, *args, **options):
        num_cars_to_create = 100
        for _ in range(num_cars_to_create):
            maker, _ = Maker.objects.get_or_create(Name=fake.company())
            car_name = fake.unique.word()
            hpp = random.randint(100, 500)
            launch_date = fake.date_between(start_date="-10y", end_date="today")

            car.objects.create(
                maker=maker, car_name=car_name, hpp=hpp, launch_date=launch_date
            )

        self.stdout.write(
            self.style.SUCCESS(f"Created {num_cars_to_create} unique Car objects.")
        )
