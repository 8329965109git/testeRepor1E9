from django.contrib import admin
from .models import Maker, car


# Create a custom admin class for the Maker model
class MakerAdmin(admin.ModelAdmin):
    list_display = ["Name", "count"]

    # Define the fields to display in the admin list view
    def tag_list(self, obj):
        return ", ".join(o.name for o in obj.tags.all())

    def Name(self, obj):
        cars = Maker.objects.filter(count=obj).first()
        car_count = cars.count()
        if car_count < 2:
            car_info = ", ".join([f"{car.Name} ({car.tags} HP)" for car in cars])


# Register the Maker model with the custom admin class
admin.site.register(Maker, MakerAdmin)


# Create a custom admin class for the Maker model
class CarAdmin(admin.ModelAdmin):
    list_display = ["maker", "car_name", "hpp", "launch_date"]
    list_filter = ("launch_date",)
    search_fields = ["car_name"]


admin.site.register(car, CarAdmin)
