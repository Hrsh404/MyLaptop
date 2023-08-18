from django.contrib import admin
from django.utils.html import format_html
# Register your models here.
from . models import Car


class CarAdmin(admin.ModelAdmin):  
    def thumbNail(self,  object):   # to display the image on admin view
        return format_html("<img src='{}' width='40' style=  'border-radius: 5px;' />" .format (object.car_photo.url))

    list_display=("id", "thumbNail",'car_title', "city", "color", "model", "fuel_type", "is_featured")
    list_display_links= ("id", "thumbNail",   "car_title", )  
    search_fields=("id",  "car_title",  "city", "model", "body_style")
    list_filter=("city", "model", "body_style","price")


admin.site.register(Car,CarAdmin) 
