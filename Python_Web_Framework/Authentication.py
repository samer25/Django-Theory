"""
Authentication is the act of proving an assertion such as the identity of a computer system user
In contrast with identification authentication is the process of verifying that identity
It might involve validating personal identity documents verifying the authenticity of a website with
a digital certificate, etc.


How Authentication Work?

During authentication credentials provided by the user are compared to those in a database of authorized
users information

If the credentials match the process is completed and the user is granted access
Authenticating a user with a user ID and a password is the most basic type of authentication
but there are more authentication factors


Authentication Factors

An authentication factor represents some piece of data or attribute that can be used to authenticate a user requesting
access to a system
Since authenticating a user with a user ID and a password relies on just one authentication factor
it is a type of single-factor authentication
Two-factor authentication usually depends on the knowledge factor combined with either a biometric factor
or a possession factor like a security token


Sessions and Cookies

Cookies and Sessions are used to store information
Cookies are only stored on the client-side machine
A session creates a file on the server where registered session variables are stored
Cookies are text files stored on the client computer


What is Authorization?

Authorization includes the process through which an administrator grants rights to authenticated users
The privileges and preferences granted for the authorized account depend on the users permissions
The settings defined for all these environment variables are set by an administrator


Authentication in Django

Django comes with a user authentication system
It handles user accounts, groups, permissions and cookie-based user sessions
The Django authentication system handles both authentication and authorization


The User Model

User objects are the core of the authentication system
They interact with your site and are used to restrict access, register usr profiles,
associate content with creators etc.
The primary attributes of the default user are:
-username
-password
-email
-first_name
-last_name


Create User

To create a new User, we can user the built-in helper function create_user()

from django.contrib.auth.models import User
user = User.object.create_user('peter', 'peter@gmail.com', 'peterpass')

Or using the Django Admin


Authenticating User

We can use the authenticate() function to verify credentials for login
If the credentials are not valid, None is returned

from django.contrib.auth import authenticate
user = authenticate(username='peter', password='peterpass')
if user: ---> Credentials are valid
    pass
else: ---> Credentials are not valid
    pass


Logout a User

from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    redirect('index')


Permissions and Authorization
Django Permissions in Users

In Django we have some built-in permission
We can manage those permissions using the Django Admin


Django Permissions in Groups

Instead of managing the permissions of each User we can use Groups
For example we can create a group User and each new User will belong to that group
Then we can add permissions to that Group so it applies to each member of the Group
That can be done in Django Admin "Groups"


Using Built-in Decorators

There are some built-in decorators in Django which allow us to add permission control

from django.shortcuts import render
from django.contrib.auth.decorators import login_required ---> The decorator check whether there is a logged in user
from app.forms.login import LoginForm

@login_required(login_url='login')
def index(request):
    return render(request, 'index.html)

def login(request):
    form = LoginForm()
    return render(request, 'login.html', {'form': form})


Creating Custom Decorators

We can make our custom decorators that will validate if a user has given permission
To do that we create a decorators.py file in our app
For example if we want to show articles only if the user has permission (belongs to the User group)
we can create a decorator function that makes the validation

Example:

decorators.py:

from django.http import HttpResponse
from django.shortcuts import render

def allowed_groups(allowed_roles=[]):
    def decorator(view_func):
        def wrapper(request, *args, **kwargs):
            group = None
            if request.user.group.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
            return HttpResponse('You are not allowed to view the articles')
        return wrapper
    return decorator

views.py:

from .decorators import allowed_groups

@allowed_groups
def index(request):
    articles = Articles.objects.all()
    return render(request, 'index.htm', {'articles': articles)

"""