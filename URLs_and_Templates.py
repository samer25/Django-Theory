"""
What is url

A Uniform Resource Locator(url) is a reference to a web resource that specifies its location on a network and a
mechanism for retrieving it
A url is a specific type of URL(Uniform Resource Identifier) although many people use the two terms interchangeably


URL structure:
https://www.example.com/blog/page-name

https - protocol
www - subdomain
example - root domain
com - top level domain
blog - subdirectory
page-name - file name

In Django we use the path function from django.url
After creating your project, in the urls.py there are already some Url configurations

from django.contrib import admin
from django.urls import path

urlpatterns = [
        path('admin/', admin.site.urls),
        ]
"""

"""
The views.py file

In the view.py file of our application we implement the logic that needs to happen when a given URL is reached
The names of the functions are usually related to the URL that is being reached

Simple Example

In views.py (in the app):

from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('It Works!')
    
------------------
In urls.py(in the project)

from django.contrib import admin
from django.urls import path
from {app_name} import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', views.index)
    ]
"""

"""
The urls.py file
(Creating urls.py file for each app)

In the urls.py file you configure what function or logic should be executed when accessing a given URL in your Apps
Usually every app you have in your project has its own urls.py file
The file can then be imported in your project urls.py file using the include function

Simple Example
Using the previous Example we can refactor the code to use include

In urls.py(in the app)

from django.urls import path
from {app_name} import views

urlpatterns = [
    path('', views.index)
    ]
    
In urls.py(in the project)

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', include('{app_name}.urls')
    ]  
"""

"""
Template
(Generate HTML Dynamically)

Being a web framework Django needs a convenient way to generate HTML dynamically
The most common approach relies on templates
A template contains the static parts of the desired HTML  output as well as some special syntax describing how dynamic
content will be inserted


Creating a Template Folder
In order to use templates we need a special folder where we create them
After the folder is created you have to add some configuration in the settings.py file
For the purpose we define a TEMPLATES_DIR variable which stores the path to the templates folder

Configuring the Templates Directory

In settings.py
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')

TEMPLATES = [
    {
    'BACKEND': ........................... ,
    'DIRS': [TEMPLATES_DIR], - adding the variable
    'APP_DIRS':True,
    ......... etc.
    }
    ]
    


Now you can create .html files that will be the templates

template/index.html

<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Django App</title>
</head>
<body>
<h1>The App Works!</h1>
</body>
</html>

Rendering a Template
Now that we created a template we want to refactor the views.py file in app

app/view.py

from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

Insead of using HttpResponse we can now use the render function what will show the template we created


Adding Context

The render function can receive a context which is a dictionary passed to the template
We can then use this dictionary to display data dynamically in the template
We use {{}} as a syntax for dynamically rendering data in the templates

app/view.py

from django.shortcuts import render

def index(request):
    context = {
        'app_name': 'My first app'
    }
    return render(request, 'index.html', context=context)

template/index.html

<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Django App</title>
</head>
<body>
<h1>The {{app_name}} Works!</h1>
</body>
</html>
"""

"""
Basic Template Logic

As in our python code in the templates we can also have programming logic
Using programming logic in the templates allows us to render different html based on some conditions
 
 
Simple Example (if statement)

template/index.html if statement

<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Django App</title>
</head>
<body>
{% if user %}
    <!-- Some html if True -->
{% else %}
    <!-- Some html if False -->

{% endif %}
</body>
</html>


Simple Example (for loop)

template/index.html if statement

<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Django App</title>
</head>
<body>
{% for user in users %}
    {{ user.username }}
{% endfor %}
</body>
</html>
"""
