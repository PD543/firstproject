from django.contrib import admin
from .models import *

# Register your models here.


#  here superuser have all the rights..
admin.site.register([Person, College, Principal, Department, Student, Subject])  #if we don't give this then we don't get table name in django administration dashboard
# Here we need to provide values in list..because if we give values directly then it will positional error

# here which ever table or class that needs to be displayed on admin page after runserver..then we need to import here