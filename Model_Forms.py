"""
The ModelForm Class

In most cases when we have a database-driven app the forms we crate overlap with our models
In this case we might want to skip defining the field types of our forms because we already defined them in the model
For this reason we use the ModelForm helper class

from django.forms import ModelForm
from my_app.models import Book

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'pages', 'author']


Using Model Forms

Create a Book Model
First we crate a simple model called Book

from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=20)
    pages = models.IntegerField(default=0)
    descriptions = models.CharField(max_length=100 default="")
    author = models.CharField(max_length=20)

Creating the Model Form
After that we create the model form

from django import forms
from app.models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__' ---> Include all fields from the model
        widgets = { ----> Add styling bootstrap
                'title': forms.TextInput(attrs={'class': 'form-control' }),
                'pages': forms.NumberInput(attrs={'class': 'form-control'}),
                'author': forms.TextInput(attrs={'class': 'form-control'}),
                'description': forms.Textarea(attrs={'class': 'form-control'})
                }


Create View

def create(request):
    if request.method == 'GET':
        form = BookForm()
        return render(request, 'create.html', {'form': form})
    else:
        form = BookForm(request.Post)
        if form.is_valid():
            book = form.save()
            book.save()
            return redirect('index')

Edit View

def edit(request, id):
    book = Book.object.get(pk=id)
    if request.method == 'GET':
        form = BookForm(instance=book)
        return render(request, 'edit.html', {'form': form})
    else:
        form = BookForm(request.Post, instance=book)
        if form.isvalid():
            book = form.save()
            book.save()
            return redirect('index')


Validating Model Forms

There are two ways to make form validation in ModelForm
-Validation in the Model
-Validation in the Form
To validate a form we can override the clean() method
To validate the model we can create custom field validators

Validating the Form

To make form validations we can override the clean() method

In Model Form BookForm:
def clean(self):
    if not isinstance(self.cleaned_data['page'], int):
        raise ValidationError('Pages must be a number')
    if self.cleaned_data['pages'] <=  0:
        raise ValidationError('Pages cannot be zero or negative')
    return self.cleaned_data


We can make a validators.py file that will contain out validation functions
validators.py:

from django.core.exceptions import ValidationError

def pages_validator(value):
    if value <= 0:
        raise ValidationError('Pages cannot be zero or negative')

After that we can add the validator in our model

from django.db import models
from app.validators import pages_validator

class Book(models.Model):
    title = models.CharField(max_length=20)
    pages = models.IntegerFields(default=0, validators=[pages_validator])
    .....
"""