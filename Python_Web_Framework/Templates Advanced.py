"""
Template Inheritance
(block, endblock, extends)

Template inheritance allows us to build a base skeleton template
The base template contains all the common elements and defines block that child templates can override
Typically header, footer, etc. remain the same in the whole app
Using template inheritance we can reuse the common parts of our app

Example Template inheritance:

base.html:

<!DOCTYPE HTML>
<html lang="en">
<head>
    <link ref="stylesheet" href="style.css">
    <title> My Site </title>
</head>
<body>
    {% block content%}
    {% endblock %}
</body>
</html>


blogs.html:

{% extends "base.html" %}
{% block content %}
    {% for entry in blog_entries %}
        <h2> {{ entry.title }} </h2>
        <p> {{ entry.body }} </p>
    {% endfor %}
{% endblock %}


Using include in templates

We can also ise the include tag to include an existing template

blogs.html:

{% extends "base.html" %}
{% block content %}
    {% for entry in block_entries %}
        {% include "blog_header.html" %}
        <h2> {{ entry.title }} </h2
        <p> {{ entry.body }} </p>
    {% endfor %}
{% endblock %}



Built-in Filters

Filters allow us to modify variables before displaying them in the browser
For example {{ name|lower }} displays the value of name variable after being filtered through the lower filter
We use a pipe "|" to apply a filter

Chained Filters

Filters can also be "chained"
The output of one filter is applied to the next

{{ text|escape|linebreaks }}  ----> Escaping text contents and converting line breaks to <p>


Filters with Arguments

Some filters require arguments
We use colon ":" to mark arguments

{{ description|truncatewords:30 }} ---> Will display the first 30 chars of description variable


Some Built-in Filters

{{ my_date|date:"Y-m-d" }} ----> formats date according to format

{{ value|default:"empty" }} ---> uses the given default if a value is False

{{ value|join:", " }} ----> joins a list with a string (like str.join(list) in python)

{{ value|length }} ---> returns the length of the value




Custom Filters
Creating templatestags Folder

In your application create a templatestag module with your custom filter file
Write your oun filter function

my_filter.py:

from django import template

register = template.Library()

@register.filter(name="odd")
def odd(nums):
    "My custom filter" --> comment
    return [x for x in muns if x % 2 == 1]



Load the filter in your template and use it
In Html:
{% extends 'index.html %}
{% load my_filter %}
{% block content %}
    {% for num in nums|odd %}
        <p> {{ num }} </p>
    {% endfor %}
{% endblock %}



Template Tags

A template tag is a function which accepts one or more arguments processes those values
and returns a value to be displayed
We already know some of the built-in template tags
-for
-if/else

{% if user %}
 <h1> Welcome User! </h1>
{% else %}
 <h1> Please, login! </h1>
{% endif %}


Template Tags Helper Functions

Django provides us with helper functions that allow us to create our custom template tags
-simple_tag - processes the data and returns a string
-inclusion_tag - processes the data and returns a rendered template
-assignment_tag - processes the data and sets a variable in the context


Creating Custom Template Tags

To create a custom template tag, we need again crate a templatetags package
Here is an example of an inclusion custom tag

my_tags.py:

from django import template
from example_app.modules import Article

register = template.Library()

@register.inclusion_tag('articles.html')
def show_articles():
    articles = Article.object.all()
    return {'articles': articles}

Using the Template Tag

Create the 'article.html' template and make a loop through the articles
After that use your tag in your main  template

articles.html:
<ul>
    {% for article in articles %}
        <li> {{ article.title }} </li>
    {% endfor %}
</ul>

Then in main template 'index.html'

<h1> Home Page </h1>
{% show_articles articles %}
"""