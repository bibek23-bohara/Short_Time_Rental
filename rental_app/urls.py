from django.urls import path
from rental_app import views

urlpatterns = [
    path('', views.index, name='index'),
    # Add any other URL patterns as needed
]