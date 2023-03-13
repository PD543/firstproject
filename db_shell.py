# here we need to import models for which we need to perform operations

# this file is not automatically generated, we need to create this file, as on console we cannot store the query and its result

from app1.models import Person

# Objs = Person.objects.all() #so to run this we need run a command - as this is related to django framework and not directly to python

# # here objects is mediator where it fetchs all data from Person table

# # here Person.objects.all() this returns queryset, so we can convert it into list
# obj_list = list(Objs)
# print(obj_list)

# first we need to go inside db shell, before exeute the this file
# on console - py manage.py shell
# then we need to execute - Django_Project\first_project
# exec(open(r"filename_path").read())

# for eg
# exec(open(r"F:\Python programs\Django_Project\first_project\app1\db_shell.py").read())

# To fetch all the persons from person table.


# Objs = Person.objects.all()
# obj_list = list(Objs) #here we get objects list, objects in the term of persons record name..to see entire record of the person we need to use dendur method

# for person in obj_list:
#     print(person.__dict__)


# To fetch single records from person table

# One = Person.objects.first()
# print(One)

# To fetch id records from person table

# record_id = Person.objects.get(id = 2)
# print(record_id)

# here when id = 4 is not present it gives error, but error is for models file so we need to use try - except block there

# try:
#     record_id = Person.objects.get(id = 4)
#     print(record_id)
# except Person.DoesNotExist:
#     print("This id is not available")

# app1.models.Person.DoesNotExist: Person matching query does not exist.

# to get multiple records we need to use filter method

# objs = Person.objects.filter(address = 'Pune' )
# print(list(objs))
# print(objs.query) # Here this gives backend query

# objs = Person.objects.filter(address = 'Pune', age = 27 ) #here ',' means and..that two condition is applied 
# print(list(objs))


# Modify existing data

# p1 = Person.objects.get(id = 1)
# print(p1.__dict__)
# print(p1.mobile_num) #to fetch individual field of that particular record

# p1.mobile_num = 988988900 #here we are updating mobile_num

# p1.save() #this needs to be saved to get reflect updated fields in db..it is like commit


# to delete record
# p1 = Person.objects.get(id = 5)
# print(p1.__dict__)
# p1.delete()
# print(p1.__dict__)

# To create objects, we can create in three ways


# First way

# p1 = Person(name= "ABC", age= 29, mobile_num = 222, address = 'Satara')
# p1.save()

# Second way

# Person.objects.create(name= "XYZ", age= 31, mobile_num = 2200, address = 'Nashik')
# so in this case no need to save..it automatically gets record create in db

# print(dir(Person.objects))

# To create_bulk record

# p1 = Person(name= "PQR", age= 29, mobile_num = 222, address = 'Satara')
# p2 = Person(name= "TQR", age= 25, mobile_num = 111, address = 'Pune')
# p3 = Person(name= "POP", age= 19, mobile_num = 333, address = 'Dhule')
# p4 = Person(name= "IOP", age= 39, mobile_num = 444, address = 'Nanded')
# p5 = Person(name= "YUI", age= 41, mobile_num = 555, address = 'Kolhapur')

# Person.objects.bulk_create([p1, p2, p3, p4, p5])

# To count records in the table

# print(Person.objects.count())

# # to delete multiple records

# Person.objects.filter(address = 'Pune').delete()

# to delete all records

# Person.objects.all().delete()


# the record startswith = A

# print(Person.objects.filter(name__startswith = "A"))
# Person.objects.filter(name__st)
# the record endswith = A

# print(Person.objects.filter(name__endswith = "Z"))

# to exclude the records, here whoes name ends with Z, there record will not get fetch

# print(Person.objects.exclude(name__endswith = "Z"))

# to check whether record is exists..it is used with filter only

# print(Person.objects.filter(id= 1).exists())

# display fetch record with the help for user defined show_deatials

# Person.objects.get(id = 2).show_details()

# for per_obj in Person.objects.all():
#     per_obj.show_details()


# for per in  Person.get_data_above_age():
#     per.show_details()


# here we can fetch only name field

# res = Person.objects.all().values() # .values() returns all records in dict type
# for i in res:
#     print(i, type(i))

# to fetch all the name field of all records in list

# res = Person.objects.all().values('name') #here we are only fetching
# name_list = []
# for i in res:
#   name_list.append(i['name'])
# print(name_list)



# res = Person.objects.all().values('age')
# print(list(map(lambda x:x['age'],res)))


# calculate the average age
# res = Person.get_age()
# print(res)

# values_list

# data = Person.objects.all().values_list() #values_list returns list of tuples with only values of all record and not the fields
# print(data)

# here we have change the database to mysql

# SO doing all the things again


from app1.models import *  # here when we want to import all the class model so we need to use '*' 
from django.contrib.auth.models import User #here this is imported to create user or superuser via code

# User.objects.create_user(username='smita', password='s') #here this creates normal user if we choose create_superuser then its superuser
# always tried to use create_user instead create
# then use py manage.py shell
# then the run code with exec....

# here are we are  changing one member is_active record to false

# p1 = Person.objects.get(id = 3)
# p1.is_active = False #here in db or mysql TRUE value be stored as 1 and false as 0
# p1.save() #here we are commiting changes in db so we need to save

# here to change multiple members to inactive....here normal it executes from left to right

# data = Person.objects.filter(id__in = [1,2]).update(is_active=False)
# print(data)


# custom manager

# print(Person.Activep.all()) #This will give active record #here after this inbuild objects manager will not work so to work that we need to add all_data = models.manager in Person class

# print(Person.all_data.all())  #here this will records


# -----------------------------------------

# here we are creating or fetch data of every class, here as we have did customization in manager so we are using 'all_data'
# as a manager
clgs = College.objects.all()
prnc = Principal.objects.all()
depts = Department.objects.all()
studs = Student.objects.all()
subjs = Subject.objects.all()

# record can be fetched based on slicing as well
# clgs = College.objects.all()[0] #here it will only give 0th index record..it means first record from DB

# print(clgs) #here we can see values because models file has commonclass which has dunder method __str__
# print(prnc)
# print(depts)
# print(studs)
# print(subjs)

# for dept in depts:
#     print(dept.__dict__)



# for stud in studs:
    # print(stud)

# for sub in subjs:
#     print(sub)

# here from college I want to know principal name so here it is one to one relationship

#---------------------------------- One to One relation


# fetch principal based on college
# clg = clgs[1] #here we are fetching college name which is present on 0th index..first college name in college table
# print(clg.principal)  #here we are getting principal name based on college name
# print(clg.principal.__dict__) 
# Note - we need to give class models name in small letters here..because in db it gets stored in small letter.


# here object.small letters mdhey another object

# one to one relation
# fetch college based on Principal

# prn = prnc[0]
# print(prn.college)

# or

# first_prin = Principal.objects.first() #here it give first record
# # print(first_prin) #here savita will be printed
# # to see savita is principal of which college
# print(first_prin.college)


# ------------------------ one to many-------------------------

# clg = College.objects.first() #one college can have multiple or many departments.
# print(clg.department_set.all()) #to access all the department of selected college we need to use 'department_set'..this can be found by doing dir(department_set)
# print(clgdir(Department))  
# here we need to use objectofone.objectofmany(smallletters)_set.all() r first()
# print(clg.department_set.first())

# dep = Department.objects.get(id= 2) #one department has many student.
# print(dep)
# print(dep.student_set.all()) #this gives all the student present in I.T


# Get the student list department wise

# depts = Department.objects.all()
# # print(dep)
# d = {}
# for dep in depts:
#     # print(f"Department - {dep} and there Student - {list(dep.student_set.all())}")
#     d[dep.name] = list(dep.student_set.all())
# print(d) #here we are creating in dictionary format

# --------------------------many to one---------------------------------

# one to one and many to one is quit similar

# here fetching datafrom many to one  -  obj_many.foreignkeynameofone

# s1 = Student.objects.get(id = 8) #here we are fetching student whoes id is 8 
# print(s1)
# print(s1.dept) #here we are displaying department name of student id 8

# get students list with department

# studs = Student.objects.all()
# for stud in studs:
#     print(f"Student name - {stud.name} and Department = {stud.dept}")


# Here there is attribute related_name available in models.py here it is nothing but a name given to overcome in built
# for example if we give related_name in one to many table we don't need to use object_set.all() instead we can use object.all directly


# few changes after adding related name to relational tables..it is recommend to always related_name to relationals table..that there should be foreign or any relational statement

# Note -- previous code won't if we change any inbuilt details..it will work with changed details

# -----------------------------------------one to one-------------------

# clg = clgs[1]
# print(clg.princi) #here we have used related_name instead of actual inbuild small letter objects scenraio
# print(clg.principal) ##this won't work now as we have modified our own related_name
# -------------------------------------one to many-------------------------


# clg = College.objects.first()
# print(clg.depts.all())
# print(clg.department_set.all()) #this won't work now as we have modified our own related_name

# depts = Department.objects.all()

# for dep in depts:
#     print(f"Department - {dep.name} and Subject - {dep.subjs.all()}")


# based on college fetch all IT students, so for this we require college, department, student

# clg = College.objects.get(id = 1) #here we require to fetch college by id
# deptss = clg.depts.all()
# print(deptss)
# dept = deptss[1]
# print(dept)
# stud = dept.studs.all()
# print(stud)

# here to optimized code

# clg = College.objects.get(id = 1)
# studs = clg.depts.all()[1].studs.all()
# for stud in studs:
#     print(stud)


# to fetch college name based on student

# stud = Student.objects.get(id = 1)
# dept = stud.dept
# clg = dept.college
# print(clg)

# stud = Student.objects.get(id = 1)
# clg = stud.dept.college
# print(clg)


# --------------------------- -------------------------------

# to inse5t or add data from code to db

# College.objects.create(name = "Modern", adr = "Shivajinagar")
# College.objects.create(name = "V.I.T", adr = "Camp")

# here we can give college id in to ways

# first way

# c1 = College.objects.get(id = 3) #modern
# p1 = Principal(name = "ABC", exp = 12, qual = "B.Tech", college = c1)
# p1.save()

# second way we cannot pass id directly for eg
# p1 = Principal(name = "ABC", exp = 12, qual = "B.Tech", college = 4)
# p1.save() #it gives error as instance should be there as valuec so if we want to give id..then we need to give coumn name available in actual d
# here column in db is represent as college_id
# p1 = Principal(name = "ABC", exp = 12, qual = "B.Tech", college_id = 4)
# p1.save() #here college_id name is available in db


# Department.objects.create(name = "Production", dept_str = 60, college_id = 3) #here college in modal.py is having college as foreign key..so we need to use column name present in db or we need to create foreign key class instance and that need to pass that object


# Note - Foriegn key or relation fields from table parameters need to give column name present in db or instance

# Student.objects.create(name = "Sushant", marks = 90, age = 20) #here dept is set as null so, when we don't give dept_id value then it takes null as a value
# Student.objects.create(name = "Vaibhav", marks = 80, age = 24)
# Student.objects.create(name = "Pranil", marks = 70, age = 27)

# here we need to add student in department means we are add department id in dept_id of student table

# s1, s2, s3 = Student.objects.filter(id__gt= 9)
# # print(s1, s2, s3)
# prod_dept = Department.objects.get(id = 4)
# # print(dir(prod_dept.studs)) #here we add method..so with the help of add method we can add s1, s2, s3, dept_id
# prod_dept.studs.add(s1, s2, s3) #here one to many ---add student in department


# we can use select_related in foreign relational query.it is recommend to use to run the query in optimized way

# studs = Student.objects.all() #in background one query is made for this
# for stud in studs: #in background it generates normal query
#     print(stud.dept) #here we are fetching department name based on student relation many to one
# and another query for this statement..so as we have used for loop so for each iterator query as background is newly created

# but here in background this code runs different queries everytime which is not recommeded
# so to overcome this we can use select_related()

# optimized way-------------------------------------
# select_related obtains all data at one time through multi-table 
# join Association query and improves performance by reducing the number of database queries. 
# It uses JOIN statements of SQL to optimize and improve performance by reducing the number 
# of SQL queries
# here only for below line all the query of student and department is created..so it does not  repeat the query
# studs = Student.objects.select_related("dept") #in background it executes joins query
# for stud in studs:
#     print(stud.dept)

# print(dir(studs.dept))


# here if we want fetch query based on offset or slicing

# studs = Student.objects.all()[1:3] #here records index start from 0 and in db it starts at 1
# for stud in studs:
#     print(stud)

# -------------------------------------------Many to Many--------------------------------
# implement many to many on student and subject
# here we are implementing another example from google to understand the many to many

# Multiple records in a table are associated with multiple records in another table.

# here in db there will be three table gets created as there is many to many relation 
# fueltype, carmodel, and third table is combination of fueltype and carmodel the table name is carmodel_fueltype

# to insert records in carmodel

# CarModel.objects.create(name = "c180")
# CarModel.objects.create(name = "c200")
# CarModel.objects.create(name = "c200", fueltype = "hbybrid") #here fueltype is many to many, we cannot direct assign value to this field

# to fetch all records from Carmodel

# carmodels = CarModel.objects.all()
# print(carmodels)


# to insert records in fueltype

# FuelType.objects.create(name = "gas")
# FuelType.objects.create(name = "petrol")
# FuelType.objects.create(name = "deisel")

# to fetch all records from FuelType
# FuelTypes = FuelType.objects.all()
# print(FuelTypes)

# here we are third table which is automatically created as many to many relation

# c180 = CarModel.objects.get(name = "c180")
# gas = FuelType.objects.get(name = "gas")
# petrol = FuelType.objects.get(name = "petrol")
# deisel = FuelType.objects.get(name = "deisel")
# c180.fueltype.add(gas) #here we are adding or inserting data in third table many to many
# c180.fueltype.add(petrol)
# c180.fueltype.add(deisel)
# print(c180.fueltype.all()) 

# here to insert record in third table we need to use instance of the class which has many relation.fieldofmanyrelation.add(instance of another associated class)

# c200 = CarModel.objects.get(name = "c200")
# c200.fueltype.add(gas)
# print(c200.fueltype.all())

# print(FuelType.objects.all())


# fetch the carmodel for fueltype gas
# so here the relation is one carmodel can have many fueltype..so we can use query as we use in 1 to M relation

# print(gas.carmodel.all())

# result = CarModel.objects.filter(fueltype__name = "gas") #here 
# print(result)

# to remove the fueltype from carmodel

# c180.fueltype.remove(gas)
# print(c180.fueltype.all())


# ...............................................................................................................................


# exec(open(r"F:\Python programs\Django_Project\first_project\app1\db_shell.py").read())

# Here we till now used orm queries to perform operations...but we can import django db and perform normal queries as well

# here in settings.py we have used django_mysql..so operation will be performed on that db


# this concept is also called as raw sql..because we are not hitting orm queries
# from django.db  import connection

# cursor = connection.cursor()
# cursor.execute('''select * from student''')
# data = cursor.fetchall()
# print(data) #here it gives data in tuple of tuple
# data = cursor.fetchmany(3) #here it fetchs 3 records
# print(data)

# another way can be using raw method

# .raw() return a set of rows from the database if not return rows, error will result.

# row_set = Student.objects.raw("Select * from student")
# print(list(row_set))
# for row in row_set: #raw returns rows so we need to use for loop
#     print(row.marks)


# multiple database -

# till above we were using only one database..but in actually work environment we need different db simulatenously

# multitenant is concept were we gather different databases

# here to use anyother db then the default we need to store that db details as a dictionary in settings.py file inside DATABASES

# if we perform normal query then it will be performing on default db ...so to perform query on another db we need to make few changes.

# py manage.py migrate --database=db_name another than default (migration on extradb defined in settings.py)

# now to use another db for manipulation below syntax needs to be used

SECONDDB = 'second_db'

# data = Student.objects.using(SECONDDB).all()
# print(data)

# c1 = College.objects.using(SECONDDB).create(name = 'V.I.T', adr = 'Kondwa')
# d1 = Department.objects.using(SECONDDB).create(name = 'I.T', dept_str = 60, college = c1)
# s1 = Student.objects.using(SECONDDB).create(name = 'Amol', marks = 60, age = 24, dept = d1)
# d1 = Department.objects.using(SECONDDB).get(name = 'I.T')

# sub = Subject.objects.using(SECONDDB).create(name = 'Python', is_pratical = 'True', dept = d1) #here not sure why student field values are not allowed

# adding data in third many to many table
# s1 = Student.objects.using(SECONDDB).get(name = 'Amol')
# sub = Subject.objects.using(SECONDDB).get(name = 'Python')
# sub.student.add(s1) (instance of table of many to many field declaration.many to many fieldname.add(other many to many name))
 
# datas = Student.objects.using(SECONDDB).all()
# print(datas)

# data = Student.objects.using(SECONDDB).all()
# print(data)

# c3 = College.objects.using(SECONDDB).create(name = 'M.I.T', adr = 'Lohagaon')
# c3 = College.objects.using(SECONDDB).get(id = 6)
# d2 = Department.objects.using(SECONDDB).create(name = 'Mech', dept_str = 60, college = c2)
# s2 = Student.objects.using(SECONDDB).create(name = 'Manish', marks = 50, age = 22, dept = d2)
# # d2 = Department.objects.using(SECONDDB).get(name = 'Mech')

# sub1 = Subject.objects.using(SECONDDB).create(name = 'FireSpare', is_pratical = 'False', dept = d2) #here not sure why student field values are not allowed

# adding data in third many to many table
# s1 = Student.objects.using(SECONDDB).get(name = 'Manish')
# sub = Subject.objects.using(SECONDDB).get(id = 4)
# sub.student.add(s1) #(instance of table of many to many field declaration.many to many fieldname.add(other many to many name))
# # res = sub.student.remove(s1) #here it only removes that particular records or object from stud_subj table
# print(res)
# datas = Student.objects.using(SECONDDB).all()
# print(datas)

# del1 = Department.objects.using(SECONDDB).get(id = 1)
# del2 = del1.delete()
# print(del2)

# col1 = College.objects.using(SECONDDB).get(id = 3).delete()
# print(col1)


# res = stud_subj = sub.student.using(SECONDDB).all().delete() #here delete records from stud_sub and student.
# print(res)

# College.objects.using(SECONDDB).get(id = 4).delete()

# Principal.objects.using(SECONDDB).create(exp= 4, qual= 'Dr', college= c3 )

# Principal.objects.using(SECONDDB).get(id = 3).delete()




# --------------------------------------------------------------------------------------------

# https://simpleisbetterthancomplex.com/tutorial/2018/08/27/how-to-create-custom-django-management-commands.html

# using the user cmd extend tool video 114

print(User.objects.all()) #here it will return queryset of User

# to create user from django shell

# User.objects.create(username = "panch", password = "vikra") #here it will create the user but the password will not be encrypted in database.i.e it will store password as it is

# User.objects.create_user(username= "hion", password= "opop", email="v@gmail.com") #here create_user encrypt the password in the db

# here we can create our own command like in build for eg py manage.py runserver ..etc...here in this case it behavious like command line argument

# We can create our own commands for our apps and include them in the list by creating a management/commands directory inside an app directory

# app1 inside it create management folder then inside management folder create commands folder inside it create my_custom_command.py

# to execute it we need to pass cmd arguments for eg python manage.py my_custom_command


# here folder name/foldername/filename must be same i.e management/commands/filename.py (filename can be anything)