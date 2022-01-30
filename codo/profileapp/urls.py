from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('<int:id>/', views.profile, name='profile'),
]