from django.contrib import admin
from .models import Maker

# Create a custom admin class for the Maker model
class MakerAdmin(admin.ModelAdmin):
    list_display = ['Name']  # Define the fields to display in the admin list view

# Register the Maker model with the custom admin class
admin.site.register(Maker, MakerAdmin)
