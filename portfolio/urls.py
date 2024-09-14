from django.urls import path
from . import views 

urlpatterns = [
    path('portafolio/', views.portfolio , name="portfolio")
]

