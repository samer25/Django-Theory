"""
CBV's

A view is a callable which takes a request and returns a response
Class-based views provide an alternative way to implement views as Python object instead of function

from django.shortcuts import render
from django.views.generic import View

class IndexView(View):
    def get(self, request):
        return render(request, 'index.html)


Built-in Generic Views

Django provides some built-in generic views
-View
-TemplateView
-RedirectView
-FormView
-ListView
-CreateView, UpdateView, DeleteView
-DetailsView


CBV's vs Function Views - Pros

CBV
-Easily extended
-Can use techniques like mixins
-Handling HTTP methods in separate class methods
-Built-in generic CBV's

Function View
-Simple to implement
-Easy to read
-Explicit code flow
-Straightforward usage of decorators

CBV's vs Function Views - Cons

CBV
-Harder to read
-Implicit code flow
-Hidden code in parent classes, mixins
-Use of decorators require extra import

Function View
-Hard to extend
-Hard to reuse
-Handling HTTP method via conditional branching


Template View

A template view renders a given template with the context containing parameters captured in the URL

from django.shortcuts import render
from django.view.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'User'
        return context

urls.py:

urlpatterns = [
    path(''), views.IndexView.as_view(), name='index'), ---> in class based view we have to add after the class "as_view()"
]


List Views

A list view is used for representing a list of objects

class ArticleListView(ListView):
    context_object_name = 'articles'
    model = Article
    template_name = 'list_article.html'

html file:

<div>
    {% for article in articles %}
        <a href="{% url 'details' article.id %}"> {{article.title}}</a>
    {% endfor %}
</div>


Detail View

While this view is executing, self.object will contain the object that view is operation upon

class ArticleDetailView(DetailView):
    template_name = 'detail_article.html'
    context_object_name = 'article_detail'
    model = Article

urls.py:
    urlpatterns = [
        path('', views.IndexView.as_view(), name='index'),
        path('article/' views.ArticleListView.as_view(), name='articles'),
        path('details/<int:pk>', views.DetailView.as_view(), name='details')
    ]

html file:

<div>
    {{ article_detail.title }}
    {{ article_detail.content }}
</div>


CRUD Views

A Create view displays a form for creating an object
An Update view display a form for editing an existing object
A Delete view displays a confirmation page and deletes an existing object

class ArticleCreateView(CreateView):
    fields = '__all__'
    model = Articles
    template_name = 'create_article.html'

class ArticleUpdateView(UpdateView):
    fields = '__all__'
    model = Article
    template_name = 'update_article.html'

class ArticleDeleteView(DeleteView):
    fields = '__all__'
    model = Article
    template_name = 'delete_article.html'
    success_url = reverse_lazy('app:articles') ---> Action on success


Set up absolute URL

When using a CreateView we need to use a function in the model called
get_absolute_url()
We use it to tell Django how to calculate the canonical URL for an object

class Article(model.Model):
    title = models.CharField(max_length=10)
    content = models.CharField(max_length=50)

    def get_absolute_url(self):
        return reverse('app:details', kwargs={'pk': self.pk}) ---> Render the details view after creation

"""