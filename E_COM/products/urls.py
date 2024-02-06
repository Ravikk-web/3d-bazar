from django.urls import path
from products import views

urlpatterns = [
    path("product_index/", views.product_index, name="product_home"),
    path("product_profile/<str:st>/", views.product_profile, name="product_profile"),
    path("product_buy/<str:st>/", views.product_buy, name="product_buy"),
]
