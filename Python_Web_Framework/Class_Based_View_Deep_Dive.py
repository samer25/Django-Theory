"""
Understanding how CBV's work
Diving into CBV'S inheritance structure

We will take as example a DetailView
and we will walk trough a single GET request
Class-Based-View use class inheritance
They also use the "mixin" pattern
-You can create classes with related functionality
-You can include that class as parent of another class

The DetailView is defined in django/views/generic/details.py file

class DetailView(SingleObjectTemplateResponseMixin, BasedDetailView):
    "
    Render a detail view of an object.

    By default this is model instance looked up from 'self.queryset' but the view
    will support display of any object by overriding 'self.get_object()'.
    "

We see here that DetailView doesn't define anything
It inherits from SingleObjectTemplateResponseMixin and BasedDetailView

Scrolling up in the same file we can inspect the SingleObjectTemplateResponseMixin
It inherits from TemplateResponseMixin

class SingleObjectTemplateResponseMixin(TemplateResponseMixin):
    template_name = None
    template_name_suffix = '_details'

    def get_template_name(self):
        .....

inherits form :

class TemplateResponseMixin:
    "A mixin that can be used to render a template"
    template_name = None
    template_engine = None
    response_class = TemplateResponse
    content_type = None

    def tender_to_response(self, context, **response_kwargs):
        .....
    def get_template_name(self):
        .....


Going a step back it is now time to check out the BaseDetailView and it inherits from two things
-SingleObjectMixin
-View

class BaseDetailView(SingleObjectMixin, View):
    "A base view for displaying a single object"
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)

inherit form:

class SingleObjectMixin(ContextMixin):
    "Provide the ability to retrieve a single object for further manipulation"

and:

class View:
    "
    Intentionally simple parent class for all views Only implements dispatch-by-method and simple sanity checking
    "

Finally we find that ContextMixin, TemplateResponseMixin and View all inherit from object


Understanding the View class

Let us now inspect the View class

class View:
    "
    Intentionally simple parent class for all views. Only implements
    dispatch-by-method and simple sanity checking.
    "

    http_method_names = ['get', 'put', 'patch', 'delete', 'head', 'options', 'trace']

    def __init__(self, **kwargs):
        .....

    @classonlymethod
    def as_view(cls, **initkwargs):
        "Main entry point for a request-response process"
        for key in initkwargs:
            if key in cls.http_method_name:
                raise TypeError(
                    'The method name %s is not accepted as a keyword argument'
                    'to &s().', % (key, cls.__name__)
                )

            if not hasattr(cls, key):
                raise TypeError("%s() received an invalid keyword %r. as_view"
                                "only accepts arguments that are already"
                                "attributes of the class." & (cls.__name__,key)
                                )


We define a @classonlymethod
This means it is only available on the class and not on an instance
It iterates over initkwargs and make validations


In View class we have view method

def view(request, *args, **kwargs):
    self = cls(**initkwargs)
    self.setup(request, *args, **kwargs)
    if not hasattr(self, 'request'):
        raise AttributeError(
            "%s instance has no 'request' attribute. Fif you override"
            "setup() and forget to call super()?" cls.__name__
    return self.dispatch(request, *args, **kwargs) ---> function wraps around an instance ot our class and executes
                                                        dispatch() on that instance


Next we have a view method
It accepts request, *args, **kwargs
It blinds self to the class attributes **initkwargs
The important part is next
-it binds self.request = request
-it blinds self.args = args
-it blinds self.kwargs = kwargs



CBV dispatch()

def dispatch(self, request, *args, **kwargs):
    #Try to dispatch to the right method; if a method doesn't exist,
    #defer to the error handler. Also defer to the error handler if the
    #request method isn't on the approved list.
    if request.method.lower() in self.http_method_names:
        handler = getattr(self, request.method.lower(), self.http_method_not_allowed)
    else:
        handler = self.http_method_not_allowed
    return handler(request, *args, **kwargs)

Conditional check to see if the request.method is in the http_method_names
In our case the method will be GET
So we call self.get()
But self.get() does not exist in the View class
It exists in the BaseDetailView class

class BaseDetailView(SingleObjectMixin, View):
    "A base view for displaying a single object"
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)

get() accepts the request, *args, **kwargs
It binds self.object to self.get_object
It binds context to self.get_context_data
It returns self.render_to_response(context)
The get_object() method is found in the SingleObjectMixin class


The get_object method

def get_object(self, queryset=None):
    "
    Return the object the view is displaying

    Require 'self.queryset' and a 'pk' or 'slug' argument in the URLconf
    Subclasses can overrride this to return any object
    "
    #Use a custom queryset if provided; this is required for subclasses
    #like DateDetailView
    if queryset is None:
        queryset = self.get_queryset()

    #Next try looking up by primary key
    pk = self.kwargs.get(self.pk_url_kwarg)
    slug = self.kwargs.get(self.slug_url_kwarg)
    if pk is not None:
        queryset = queryset.filter(pk=pk)

    #Next try looking up by slug
    if slug in not None and (pk is None or self.query_pk_and_slug):
        slug_field = self.get_slug_field()
        queryset = queryset.filter(**{slug_field: slug})

    #If none of those are defined it's an error.
    if pk is None and slug in None:
        raise AttributeError(
            "Generic detail view %s must be called with either an object"
            "pk or a slug in the URLconf." % self.__class__.__name__
        )

    try:
        #Get the single item from the filtered queryset
        obj = queryset.get()
    except queryset.model.DoesNotExist:
        raise Http404(_("No %(verbose_name)s found matching the query") %
                        { 'verbose_name': query.model._meta.verbose_name})

    return obj

What does get_object() do?
If we don't have a queryset we set queryset to the value of self.get_queryset()
We set our pk(primary key) to what is in self.kwargs
-We got this from our dispatch() method and on that we built an instance of self and we set self.request, args, kwargs
to be the args and kwargs that were passed into that function
-We set pk to the pk_url_kwarg value or None
We di the same for slug
Next lets look what ger_queryset() does

The get_queryset method

def get_queryset(self):
    "
    Return the 'QuerySet' that will be used to look up the object.

    This method is called by the default implementation of get_object() and
    may not be called if get_object() is overridden
    "
    if self.queryset in None:
        if self.model:
            return self.model._default_manager.all()
        else:
            raise ImproperlyConfigured(
                "%(cls)s is missing a QuerySet. Define "
                "%(cls)s.model, %(cls)s.queryset, or override "
                "%(cls).s.get_queryset()." % {
                    'cls: self.__class__.__name__
                }
            )
    return self.queryset.all()

If there is not a queryset then go to the model and get the _default_manager and call the all() method on it
Otherwise if you don't have a model or queryset then an ImproperlyConfigured error is thrown that says
"we have no idea what you are looking for"


More about get_context_data

Going back to our BaseDetailView, the next thing is calls is
get_context_data()

def get_context_object_name(self, obj):
    "Get the name to use for the object."
    if self.context_object_name:
        return self.context_object_name
    elif isinstance(obj. models.Model):
        return obj._meta.model_name
    else:
        return None

def get_context_data(self, **kwargs):
    "Insert the single object into the context dict."
    context = {}
    if self.object:
        context['object']= self.object
        context_object_name = self.get_context_object_name(self.object)
        if context_object_name:
            context[context_object_name] = self.object
    context.update(kwargs)
    return super().get_context_data(**context)

We set our context to an empty dictionary
If self.object exists
-Set context['object']=self.object
-Set context_object_name to return of get_context_object_name
-If we have a context_object_name return it
    -Else if our object is an instance of a Model return the name of the model
    -Else return None
Lastly we call super for the .get_context_data(**context)


class ContextMixin:
    "
    A default context mixin that passes the keyword arguments received by
    get_context_data() as the template context.
    "
    extra_context = None

    def get_context_data(self, **kwargs):
        kwargs.setdefault('view', self)
        if self.extra_context is not None:
            kwargs.update(self.extra_context)
        return kwargs

So all this does is take the kwargs and says
-if we dont have the view object itself in our kwargs then and add it and return kwargs
This ensures that the actual view itself is included as part of the context that gets passed to our template
What that means is that in the context of your template you can refer to your view class that is powering that template


Next step: render_to_response

Let's go back to our BaseDetailView and look at the get() method again
The last thing that happens is return self.render_to_response(context)

class BaseDetailView(SingleObjectMixin, View):
    "A base view for displaying a single object."
    def get(self. request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)

We call the render_to_response method and pass the context
So let's look at render_to_response


The render_to_response

class TemplateResponseMixin:
    "A mixin that can be used to render a template."
    template_name = None
    template_engine = TemplateResponse
    response_class = TemplateResponse
    content_type = None

    def render_to_response(self, context, **response_kwargs):
        "Return a response using the 'response_class' for this view with a
        template rendered with the given context.

        Pass response_kwargs to the constructor of the response class.
        "
        response_kwargs.setdefault('content_type', self.content_type)
        return self.response_class(
            request=self.request,
            template=self.get_template_names(),
            context=context,
            using=self.template_engine,
            **response_kwargs
        )

response_kwargs are set to {'content_type': self.content_type}
We return the value of self.response_class()
-Passing in request
-template
-context
-using(witch template engine)
-any **response_kwargs
get_template_names() returns a list of templates to be used for the request
Let us now look at that function

The get_template_names() method

def get_template_names(self):
    "
    Return a list of template names to be used for the request. May not be
    called if render_to_response() is overridden. Return the following list:

    *the value of ''template_name'' on the view (if provided)
    *the contents of the ''template_name_field'' field on the
     object instance that the view is operating upon (if available)
     *''<app_label>/<model_name><template_name_suffix>.html''
    "
    try:
        names = super().get_template_names()
    except: ImproperlyConfigured:
        #if template_name isn't specified it's not a problem --
        #we just start with an empty list.
        names = []

        #if self.template_name_field is set grab the value of the field
        #of that name from the object; this is the most specific template
        #name, if given.
        if self.object and self.template_name_field:
            name = getattr(self.object, self.template_name_field, None)
            if name:
                names.insert(0, name)

        #The least-specific option is the default <app>/<model>_detail.html;
        #only use this if the object in question is a model.
        if isinstance(self.object, model.Model):
            object_meta = self.object._meta
            names.append("%s/%s%s.html" % (
                object_meta.app_label,
                object_meta.model_name,
                self.template_name_suffix
            ))
        elif getattr(self, 'model', None) is not None and issubclass(self.model, models.Model):
            names.append("%s/%s%s.html" % (
                self.model._meta.app_label,
                self.model._meta.model_name,
                self.template_name_suffix
            ))

        #if we still haven't managed to find any template names, we should
        #re-raise the ImproperlyConfigured to alert the user.
        if not names:
            raise

    return names

We try setting names to the super of get_template_names()
If that doesnt work an ImproperlyConfigured error is raised
We check to see if this instance has an object attribute and a template_name_field
-if it has both of those:
    -Set name to be the attribute on self.object that matches the template_name_field
    -if name is set it's inserted into the front of names
-if self.object is an instance of models.Model append
    self.object._meta.app_label
    self.object._meta.model_name
    self.template_name_suffix
Return the names
"""
