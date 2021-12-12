"""
What is Django REST

Django REST framework is a powerful and flexible toolkit for building Web APIs
API
-is Application Programming Interface
-defines how other components/systems can use it
-defines the kinds of calls or requests that can be made
-can provide extension mechanisms for extending existing functionalities


Why use Django REST

The reasons you might want to use Django REST are:
-The Web browsable API  is a huge usability win
-Authentication polices including packages for OAuth1a and OAuth2
-Serialization that supports both ORM and non-ORM data sources
-Used and trusted by many companies including Mozilla, Red Hat, Heroku and Eventbrite


Django Rest and RESTful APIs

Django Rest Framework lets you create RESTful APIs - a way to transfer
information between an interface and a database in a simply way

-----------------   ---------------
| Web frontend  |   | Mobile App  |
-----------------   ---------------
-----------------------------------
|        API REST SERVICE         |
-----------------------------------
--------  -------------  -------------  -------------
| DB   |  | Service A |  | Service B |  | Service N |
--------  -------------  -------------  -------------


RESTful Structure

In a RESTful API, endpoints (URLs) define the structure of the API and how
users access using the HTTP methods
- GET, POST, PUT, DELETE

Endpoint |      GET       |     POST     |        PUT       |      DELETE     |
---------|----------------|--------------|------------------|-----------------|
/books/  | Show all books | Add new book | Update all books | Delete all books|
---------|----------------|--------------|------------------|-----------------|
/books/id| Show <id>      | N/A          |  Update<id>      | Delete<id>      |
------------------------------------------------------------------------------|


Requirements and Installation

Requirements

To use Django REST Framework we need:
-Python
-Django
Usage of the officially supported and latest versions of Python and Django are highly recommended
Optional: coreapi, Markdown, Pygments, django-filter, django-quardian

Installation and Setup

To install Django REST we use the pip command

pip install djangorestframework

Next we need to add it in our INSTALLED_APPS
Setting and include the rest_framework.urls

settings.py:

INSTALLED_APPS = [
    ....
    'rest_framework',
    ]

project/urls.py
urlpatterns = [
    ...
    path('api/', include('rest_framework.urls'))
    ]


Creating Simple RESTful API
(Books API)

Creating a Model

After installing the Django REST Framework and setting it up, we will crate our Book model

from django.db import models

models.py:

class Book(models.Model):
    title = models.CharField(max_length=20)
    pages = models.IntegerField(default=0)
    description = models.TextField(max_length=100, default="")
    author = models.CharField(max_length=20)

Creating a Serializer

Serializers allow complex data to be converted to native Python data types that can then be easily
rendered into JSON, XML, etc.
Serializers also provide deserialization allowing parsed data to be converted back into
complex types

creating serializers.py in your app

from rest_framework import serializers
form .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


Creating the ListBooksView

The ListBookView will handle GET and POST
requests on localhost:8000/api/books

view.py:

from rest_framework.views import ApiView
from rest_framework.response import Response
from rest_framework import status
from .models import Book
from .serializers import BookSerializer

class ListBookView(APIView):
    def get(self, request):
        books = Book.object.all()
        serializer = BookSerializer(books, many=True)
        return Response({'books': serializer.data})

Creating the URL

Now we need to add the URL pattern

from django.urls import path
from books.views import ListBookView

urlpatterns = [
    path('books/', ListBookView.as_view(), name='books-all')
    ]


Testing the API

To run the API we use command for standard Django project

python manage.py runserver

Then navigate in browser to localhost:8000/api/books

Implement Post in the View at the class ListBookView after get() method

    ....
    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



Creating DetailBookView

The View will handle GET, POST, and DELETE method

class DetailBookView(APIView):
    def get(self, request, id):
        book = Book.objects.get(pk=id)
        serializer = BookSerializer(book)
        return Response({'book': serializer.data})

    def post(self, request, id):
        book = Book.objects.get(pk=id)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        book =Book.object.get(pk=id)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

Create the URL

On "./book/{id}" we will be able to update and delete a book

from django.urls import path
from django.views import ListBooksView, DetailBookView

urlpatterns = [
    path('book/', ListBookView.as_view(), name='book-all'),
    path('book/<int:id>', DetailBookView.as_view(), name='book-detail')
    ]
"""

