from django.db import models

# Create your models here.

class Maker(models.Model):
    Name=models.CharField(max_length=100)
    update_date=models.DateField(blank=True, null=True)
    def __str__(self):
        return self.Name

class car(models.Model):
    maker=models.ForeignKey(Maker,on_delete=models.CASCADE)
    car_name=models.CharField(max_length=100)
    hpp=models.IntegerField()
    launch_date=models.DateField()

    def __str__(self):
        return self.car_name
    

    
