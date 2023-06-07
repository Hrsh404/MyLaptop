from django.contrib import admin

from .  models import Client

from django.utils.html  import format_html  

#To show a better table view
class ClientAdmin(admin.ModelAdmin): 
    def thumbNail(self,  object):   # to display the image on admin view
        return format_html("<img src='{}' width='40' style=  'border-radius: 10px;' />" .format (object.photo.url))


    list_display=("id", "thumbNail",  "name", "createdData") # to display the data on admin view
    list_display_links= ("id", "thumbNail",   "name", )  
    search_fields=("name", ) # To search on the basis of name | comma isliye lagaya jisse value ko as a tuple le na ki as a string. 
    list_filter=("createdData", ) #Filtering on the basis of date. Date ki jagah data lika hai. kon change kare models.py se fir pura
                                  #migrate karna padeaga yr. 


admin.site.register(Client,ClientAdmin)