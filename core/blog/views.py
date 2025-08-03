from re import L
from django.shortcuts import render , redirect
from django.views.generic.base import TemplateView, RedirectView
from .models import Post
from django.views.generic import ListView, DetailView, FormView, UpdateView, DeleteView
from .forms import PostForm
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
'''
# -------------------------------
# Function-based view definition
# -------------------------------
def indexView(request):
    
    name = 'ali'
    context = {'name': name}
    
    return render(request, 'index.html', context)
'''
# -------------------------------
# Class-based view definition
# -------------------------------
class IndexView(TemplateView):
    # Specify the template to be rendered
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        # Call the parent class's get_context_data to get the default context dictionary
        context = super().get_context_data(**kwargs)
        
        # Add a custom key-value pair to the context; this will be accessible in the template
        context["name"] = "ali"
        context["posts"] = Post.objects.all()
        
        return context

'''
# -------------------------------
# Function-based view for redirect
# -------------------------------
from django.shortcuts import redirect
def RedirectToMaktab(request):
    return redirect ('https://maktabkhooneh.com')
'''

# -------------------------------
# Class-based view for redirect
# -------------------------------
class RedirectToMaktab(RedirectView):
    url = 'https://maktabkhooneh.com'
    
class PostListView( ListView):
    model = Post
    # queryset = Post.objects.all()
    
    context_object_name = 'posts'
    paginate_by = 5
    ordering = ['-published_date']

class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    context_object_name = 'post'
    
    
    
'''
class PostCreateView(FormView):
    template_name = "blog/contact.html"
    form_class = PostForm
    success_url = "/blog/post/"
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
'''    

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post 
    #fields = ['author', 'title', 'content', 'status', 'category', 'published_date']
    form_class = PostForm
    success_url = "/blog/post/"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class PostEditView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    success_url = "/blog/post/"

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = "/blog/post/"