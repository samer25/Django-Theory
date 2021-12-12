"""
Registration

A lot of the coding for working with User and Authorization happens in the views.py file
We check if there is a POST request and then perform na action based off that information
Sometimes we will want to save that information directly to the database
user.save()
Other times we set commit=False so we can manipulate the data before saving it to the database
This prevents collision errors
user.save(commit=False)


Example of a User registration

def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            pic = 'profile_pic'
            if pic in request.FILES:
                profile.profile_pic = request.FILES[pic]
                profile.save()
                registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
        return render(request, 'basic_app/registration.html' {'user_form': user_form,
            'profile_form': profile_form, 'registered': registered})


We should edit the urls.py file in our application, now that we have a view for registering

app/urls.py:

from .views import register

urlpatterns = [
    path('register/', register, name='register'),
    ]



Login/logout

Once a user is registered we want to make sure that they can log in and log out the site
This process involves:
-Setting up and the login views
-Using built-in decorators for access
-Adding the LOGIN_URL in settings
-Creating the login.html
-Editing the urls.py files


Example of a User login

from django.contrib.auth import authenticate, login, logout

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Account not Active")
        else:
            return HttpResponse('Invalid login details)
    else:
        return render(request, 'basic_app/login.html', {})

@login_required
def special(request):
    return HttpResponse("Logged in")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index')))

urls.py

from .views import register, user_login

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='user_login'),
    ]

project/urls.py:

urlpatterns = [
    path('', view.index, name='index'),
    path('admin/', admin.site.urls),
    path('app/', include('basic_app.urls')),
    path('logout/', views.user_logout, name='logout'),
    path('special/', views.special, name='special'),
    ]



Django Signals

The Django Signals is a strategy to allow decoupled applications to get notified when certain events occur
A common use case is when you extend the Custom Django User
by using the Profile strategy through a one-to-one relationship
We use a "signal dispatcher" to listen for the Users post_save event to also update
the Profile instance as well


When to Use Signals>

When many pieces of code may be interested in the same events
When you need to interact with a decoupled application, e.g.
-A Django core model
-A model defined by a third-party app


Extending the User Model

We often need to extend the Custom Django User in our applications
We will be creating a new Django Model to store extra information that relates to the User Model

from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(mac_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    We will now define signals so our Profile model will be automatically created/updated
    when we create/update User instances

    Code continues form Profile class

    @receiver(post)save, sender=User)
    def create_user_profile(sender, instance, created **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()


Updating with Django Forms

forms.py:

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('url', 'location', 'company')


views.py

@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            massages.success(request,_('Your profile was successfully updated!'))
            return redirect('settings:profile')
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
        return render(request, 'profile/profile.html', {
            'user_form': user_form,
            'profile_form': profile_form,
        })


profile.html
<form method='POST'>
    {% csrf token %}
    {{ user_form }}
    {{ profile_form }}
    <button type="submit">Save</button>
</form>
"""
