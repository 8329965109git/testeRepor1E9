# myapp/signals.py
from django.contrib.auth.signals import user_logged_in, user_logged_out
from .models import car, Maker
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(user_logged_in)
def login_success(sender, request, user, **kwargs):
    with open("login_logs.txt", "a") as log_file:
        log_file.write("---\n")
        log_file.write("Logging-in signal... Run Intro\n")
        log_file.write(f"Sender: {sender}\n")
        log_file.write(f"Request: {request}\n")
        log_file.write(f"User: {user}\n")
        log_file.write(f"Kwargs: {kwargs}\n")


@receiver(user_logged_out)
def logout_success(sender, request, user, **kwargs):
    with open("logout_logs.txt", "a") as log_file:
        log_file.write("---\n")
        log_file.write("Logging-out signal... Run Outro\n")
        log_file.write(f"Sender: {sender}\n")
        log_file.write(f"Request: {request}\n")
        log_file.write(f"User: {user}\n")
        log_file.write(f"Kwargs: {kwargs}\n")


@receiver(post_save, sender=car)
def car_created_handler(sender, instance, created, **kwargs):
    var = car.objects.filter(car_name=str(instance)).first()
    maker_id = var.maker
    cd = Maker.objects.filter(Name=str(maker_id)).first()
    cd.count += 1
    cd.save()
    # print("cdID", cd.count)
    # Assuming you have a queryset named 'var'
    # for i in var:
    #     p(i.maker)

    # print("Instance", instance)
    # print("sender", sender)
    # print("created", created)
    # print("kwargs", kwargs)
