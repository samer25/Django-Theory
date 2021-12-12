"""
Media files are pictures, music, audios, video, and documents
Computer programs or applications can read and work with digital file after it is encoded during the saving process
For instance, document formats can be read and edited in word-processing programs like  Microsoft Word


Pillow(Python Imaging Library)

Python Imaging Library (PIL in newer versions known as Pillow) is a free library
It adds support for opening manipulating and saving many different image file formats
It is available for Windows, Mac OS X and Linux
Some of the file formats supported are  PPM,PNG,JPEG,GIF, TIFF and BMP

To install pillow we can use the python package manager (pip)
>>pip install Pillow

Warnings
-Pillow and PIL cannot co-exist in the same environment
-Before installing Pillow, uninstall PIL
"""

"""
Static Files in Django
(Managing Static Files)

Most of the times your application would need to serve external files such as JavaScript, etc.
This type of files are called static files


Configuring Static Files in Django

First make sure that your application is in INSTALLED_APPS in settings.py
Make sure you have STATIC_URL variable in settings.py
STATIC_URL = '/static/'

Make sure you have STATICFILES_DIRS variable in settings
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
    ]
    

Using Static Files

To include your CSS for example you will need the following code:
{% load static %}
<link rel="stylesheet" href="{% static './css/style.css' %}"

To include images we use the same approach
{% load static %}
<img src="{% static './my_image.png' %}" alt="My image">


Media Files in Django
(Images)

Configure Media Folder
Create a media folder and configure it in the settings.py file
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/') ---> media is name of the folder that you created
MEDIA_URL = '/media/'

Create Image Field in a Model

from django.db import models

class Image(models.Model):
    image = models.ImageField(upload_to='images') ---> that will crate folder in media folder in it not exist 
    

Create a Model Form

from django.forms import ModelForm
from app.models import Image

class ImageForm(ModelForm):
    class Meta:
        model = Image
        fields = '__all__'


In view.py of the app:

def index(request):
    if request.method = "GET":
        form = ImageForm()
        return render(request, 'index.html, {'form': form})
    elif request.method = "POST"
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
        image = form.save()
        image.save()
        return render(request, 'index.html' {image': image})


In urls.py in the app

from django.conf import settings
from django.conf.urls.static import static
form .views import index

urlpatterns = [
    path('', index, name='index') 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) --> Configure the URLs for media 

In html file:
<form enctype="multipart/form-data", method="POST">
    {% crf_token %}
    {{ form.as_p }}
</form>

<div class="card m-3" style="width: 18rem";>
    <img class "card-img-top" src="{{ image.url }} alt="Cart image cap">
</div>



Media Files in Django
(Documents)

In models.py

class Document(models.Model)
    url = models.FileField(upload_to='documents')

In forms.py

class DocumentsForms(ModelForm):
    class Meta:
        model = Document
        fields = '__all__'

In html file

<form enctype="multipart/form-data", method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit"
</form>

Dont forget to passed in views.py
"""