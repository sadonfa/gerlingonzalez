from django.urls import path
from . import views

urlpatterns = [
    path('sobre-mi/', views.about, name="about"),
    path('formulario/', views.form, name="form")
]
