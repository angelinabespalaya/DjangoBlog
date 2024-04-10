from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, CreateView

from ml_model import DiabetesPredictor
from ml_model2 import DiabetesPredictor2
from ml_model3 import Iris_neiron
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin

from .utils import DataMixin
from django.shortcuts import render, redirect
from django.http import HttpResponse
import joblib
import numpy as np
from django.shortcuts import render






class Bloglist(ListView):
    paginate_by = 2
    model = Post
    template_name = 'home.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'


class RegisterUser(DataMixin, CreateView):
    form_class = UserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        return dict(list(context.items()) + list(c_def.items()))

class LoginUser(DataMixin, LoginView):
    form_class = AuthenticationForm
    template_name = 'login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')

def logout_user(request):
    logout(request)
    return redirect('login')


def predict_diabetes(request):
    if request.method == 'POST':
        predictor = DiabetesPredictor()
        predictor.train()
        input_data = {
            'MedInc': request.POST['MedInc'],
            'HouseAge': request.POST['HouseAge'],
            'AveRooms': request.POST['AveRooms'],
            'AveBedrms': request.POST['AveBedrms'],
            'Population': request.POST['Population'],
            'AveOccup': request.POST['AveOccup'],
            'Latitude': request.POST['Latitude'],
            'Longitude': request.POST['Longitude']
        }  # Replace with actual feature names



        prediction = predictor.predict(input_data)

        return render(request, 'result.html', {'prediction': prediction})

    return render(request, 'prof1.html')

def predict_diabetes2(request):
    if request.method == 'POST':
        predictor = DiabetesPredictor2()
        predictor.train()
        #['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction',
        # 'Age']

        input_data = {
            'Pregnancies': request.POST['Pregnancies'],
            'Glucose': request.POST['Glucose'],
            'BloodPressure': request.POST['BloodPressure']
        }  # Replace with actual feature names features = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness','Insulin','BMI','DiabetesPedigreeFunction','Age']

        prediction = predictor.predict(input_data)

        return render(request, 'result2.html', {'prediction': prediction})

    return render(request, 'prof2.html')


def iris(request):
    if request.method == 'POST':
        predictor = Iris_neiron()
        predictor.train()
        #['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']

        input_data = {
            'sepal length (cm)': request.POST['sepal length (cm)'],
            'sepal width (cm)': request.POST['sepal width (cm)'],
            'petal length (cm)': request.POST['petal length (cm)'],
            'petal width (cm)': request.POST['petal width (cm)']
        }

        prediction = predictor.predict(input_data)

        return render(request, 'result3.html', {'prediction': prediction})

    return render(request, 'prof3.html')