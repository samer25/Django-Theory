"""
Model Definition

A model is the single definitive source of information about your data
It contains the essential fields and behaviors of the the data you are storing
Generally each model maps to single database table
Each model is a Python class that subclasses "django.db.models.Model"
Each attribute of the model represents a database field

The models.py file

In each application we have a models.py file
In there we create all of our models that will be used in the application

from django.db import models

class Person(models.Model): ----> Model Name
    first_name = models.CharField(max_length=30) ---> fields
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()


Basic Model Fields

BooleanField - a True/False field (default for Checkboxinput)
CharField - small - to large-sized strings (used with max_length)
DateField - a date represented by datetime.date
FloatField and integerField - self explanatory
URLField - CharField for URL's (validated by URLValidator)
TextField - Large text Field (used for Textarea)


Relationship Fields

ForeignKey - Many-to-one relationship; requires two positional arguments:
-the class to which the model is related and the on_delete option
ManyToManyField - Many-to-many relationship; requires a positional argument:
-the class to which the model is related
OneToOneField - One-to-one relationship; similar to foreignKey with unique=True, but the "reverse" side of the relation
will return a single object


Set up Database(PostgreSQL)

To configure our project to work with PostgreSQL we need to set it up in the settings.py file

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql', ---> Use postgreSQL
        'NAME': 'testdb', ----> Name of the database
        'USER': 'postgres', ----> Database user credentials
        'PASSWORD': 'admin' -------|
        }
    }



Connect to PostgreSQL(IN PyCharm)

Top right click to databasee then the sign + chose Data Source then PostgreSQL
Then add username and password click to test connection then Ok


Create Database

Top right click to databasee right click to database folder then  New  then Database


Applying Changes

In order to apply the changes we made in our models we use migrations
During a migration against the database there are series of migrations that Django requires that create tables to keep
track of administrators and sessions

python manage.py makemigrations
python manage.py migrate

Django Admin

Django Admin is an automatic admin interface
It reads data from your models to provide interface where users can manage the content of the application
The admin is enabled in the default project template used by startproject

The admin.py File

In order to see the data in Django Admin we need to register all the models in a special file in our app called admin.py

from django.contrib import admin
from test_app.models import Person

admin.site.register(Person)


Access Django Admin

To access the Django Admin you need a superuser
To create a superuser we use the following command:

python manage.py createsuperuser

After that we start our project and navigate to the admin site
'localhost/admin'


Django Admin Benefits

In the Django Admin we can manage the data stored in our database
We can manually create, update and delete data from the database


The MTV Pattern (Model Template View)

MTV is a software architecture pattern that separates data presentation from the logic of handling user interactions
MTV stands for Model, Template, View
-Model - Logical data structure
-View - Data formatting and business logic
-Template - Presentation layer (data display)


CRUD(Create, Read, Update, Delete)

In computer programming create, read,update and delete (CRUD) are the four basic functions of persistent storage
Alternate works are sometimes used when defining the basic functions of CRUD
such as:
 retrieve instead of read,
 modify instead of update
 or destroy instead of delete

CRUDE in Django

Once you are created your data models Django automatically gives you a database-abstraction API that lets you
create, retrieve, update and delete objects

Create

In order to create and object we use the standard syntax for creating an object
When we are ready we just use the save() method to save the object in the database

from test_app.models import Person
person = Person(first_name="John", last_name="Smith", age=35)
person.save

Read

To get all objects
from test_app.models import Person
all_people = Person.objects.all()

To get a specific object
all_people = Person.objects.get(first_name='John')

To filter objects
all_people = Person.objects.filter(age=35)

Field lookups
all_people = Person.objects.filter(age__lte=35) ---> Less that or equal


Update

To update an object we need to retrieve it change the fields we want to and save it again

from test_app.models import Person
person = Person.objects.get(pk=1) ---> Primary Key
person.age = 36
person.save()


Delete

To delete an object we need to retrieve it and then use the delete() method to remove it from the database

person = Person.objects.get(pk=1)
person.delete()
"""