from django.urls import path
from . import views 

urlpatterns = [
    path('blog/', views.blog , name="blog"),
    path('blog/<int:id>/<slug:art_slug>/', views.article , name="blog")
]


