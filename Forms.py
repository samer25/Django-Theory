"""
HTML forms

Document which stores information of a user on a web server using interactive controls
Contains different kind of information:
-username
-password
-etc.
The elements used in an HTML form are:
-check box, input box, radio buttons, submit buttons etc.


Bound and Unbound

a Form instance is either bound to a set of data or unbound
-Bound to a set of data
    - Capable of validating that data and rendering the form as HTML with the data displayed in the HTML
-Unbound
    - Cannot do Validation


<body>
    <form action="/your-name/" method="post">
        <label for="your_name"> Your name: </label>
        <input id="your_name" type="text" name="your_name" value="{{ current_name}}">
        <input type="submit" value="OK">
    </form>
</body>
"""

"""
Django Forms
Django Forms Advantages

Quickly generate HTML form widgets
Validate data and process it into a Python data structure
Create form versions of our Models
Quickly update models from Forms

from django import forms

class FormName(forms.Form):
    name = forms.CharField()
    age = forms.IntegerField()
    

Example:

from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(max_length=100)

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)
"""

"""
Built-in Widgets

Django's representation of an HTML input element
Widgets documentation
Type of widgets:
-Textarea
-PasswordInput
It handles:
-the rendering of the HTML
-the extraction of data from GET/POST dictionary

Textarea:
Used to larger text
Able to be expanded

PasswordInput:
Converts the text into password
password: 1234566
to
password: *******


Forms with Views

CRTF token
Cross-site Request Forgery protection
Cross-site REQUEST FORGERIES
-type of malicious exploit
-unauthorized commands are performed on behalf of an authenticated users
More about Cross-site Request Forgery in: https://www.squarefree.com/securitytips/web-developers.html#CSRF
"""

"""
Custom Form Validators
Built-in Validators

Collection of callable validators
Form validation happens when the data is cleaned
Validators are functions
Takes a single argument and raises ValidationError on invalid input
Validators can be used for reusing validation logic between different types of fields


Example: Django Validators
-EmailValidator
-URLValidator
-MinValueValidator/MaxValueValidator
-MinLengthValidator/MaxLengthValidator
-RegexValidator

Bots and Bot Catchers

Bots also called "web crawlers"
Bots are software applications that run automated scripts
Perform simple and structurally repetitive tasks
-Indexing a search engine
-Gathering information much faster
Bots enter their value in inputs of the forms

Bot catchers

User created forms
User to catch malicious bots on our website

def clean_bot_catcher(self):
    bot_catcher = self.clean_data['bot_cather']
    if len(bot_cather) > 0:
        raise form.ValidationError("GOTCHA BOT!")
    return bot_catcher

"""