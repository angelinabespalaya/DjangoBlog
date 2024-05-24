from django.urls import path
from django.views.generic import ListView, DetailView

from blog.views import Bloglist, AboutPageView, BlogDetailView, RegisterUser, LoginUser, predict_diabetes, logout_user, \
    predict_diabetes2, iris

from . import views

#app_name = 'djangoProject'

urlpatterns = [
    path('post/<int:pk>/', BlogDetailView.as_view(), name = 'post_detail'),
    path('about/', AboutPageView.as_view(), name = 'about'),
    path('', Bloglist.as_view(), name = 'home'),
    path('register/', RegisterUser.as_view(), name = 'register'),
    path('login/', LoginUser.as_view(), name = 'login'),
    path('prof1/', predict_diabetes, name = 'predict_diabetes'),
    path('prof2/', predict_diabetes2, name = 'predict_diabetes2'),
    path('prof3/', iris, name = 'iris'),
    path('logout/', logout_user, name='logout'),
]

