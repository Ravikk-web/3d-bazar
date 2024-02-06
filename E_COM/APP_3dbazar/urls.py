from django.urls import path, include
from . import views

urlpatterns = [
    path('', include('authentication.urls')),
    path('', include('products.urls')),
    path("", views.home, name="home"),
    path("about", views.about, name='about'),
]
