from django.urls import path
from core import views

urlpatterns = [
    path('', views.home, name="home" ),
    path('inicio/', views.home, name="home" ),
    path('contacto/', views.contact, name="contact" ),
    path('detail/', views.detail, name="detail" )
]
