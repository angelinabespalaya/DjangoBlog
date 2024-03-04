from django.urls import path
from django.views.generic import ListView, DetailView

from blog.views import Bloglist, AboutPageView, BlogDetailView

urlpatterns = [
    path('post/<int:pk>/', BlogDetailView.as_view(), name = 'post_detail'),
    path('about/', AboutPageView.as_view(), name = 'about'),
    path('', Bloglist.as_view(), name = 'home')
]