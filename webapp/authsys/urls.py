from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.pageLogin, name='login'),
]