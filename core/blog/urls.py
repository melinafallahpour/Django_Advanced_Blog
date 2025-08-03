from django.urls import path
from . import views
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView

app_name = "blog"

urlpatterns = [
    # function-based view
    # path("fbv-index/", views.indexView, name= "fbv-index"),
    # class-based view    
    path("cbv-index/", views.IndexView.as_view(), name='cbv-index'),
    # Redirect view
    path("go-to-django/", RedirectView.as_view(url="https://www.djangoproject.com/"), name="go-to-django"),
    path("go-to-index/", RedirectView.as_view(pattern_name="blog:cbv-index"), name="go-to-index"),
    # cbv of redirect
    path("go-to-maktab/", views.RedirectToMaktab.as_view(), name="redirect_to_maktab"),
    
    
    
    path('post/', views.PostListView.as_view(), name="post-list"),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name="post-detail"),
    path('post/create/', views.PostCreateView.as_view(), name="post-create"),
    path('post/<int:pk>/edit/', views.PostEditView.as_view(), name="post-edit"),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name="post-delete"),
    
    
]
