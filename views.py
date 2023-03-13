from django.shortcuts import render, HttpResponse
from .models import Student
# from django.http im HttpResponseport

# Create your views here.

# here we write business logic in view
# there are two types of views
# function based view
# class based view

def welcome(request): #here this is similar to self..we can write anyname here
#     # print(request.method)
    stud = Student.objects.get(id = 1)
#     #below code helps to fetch request from client to the server
#     # here in url query params or quey parameter should always in dict format ..but its type is consider as string
#     print(request.GET.get('name')) #http://127.0.0.1:8000/welcome/?name=abc here request.Get.get fetch the values given by client from url or postman
    studs = Student.objects.all().values("name")
    stud = list(map(lambda x:x['name'], studs))
    print(stud)
    
    return HttpResponse(f"Welcome {stud} to view page") #this is welcome function to display this function on browser we need to add path in urls.py file

# if we need to create .html files..it needs to be created under application here app1 is our application inside it we can create template folder

def first(request):
    return render(request,'first.html') #here keep in mind python interpreter checks for 'templates' spelling showed be card..by default interpreter search for templates
#  By default, DjangoTemplates looks for a templates subdirectory in each of the INSTALLED_APPS. here if want to check templates path we need to gove in templates section under dir inside settings.py