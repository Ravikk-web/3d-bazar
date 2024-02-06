from django.urls import path,include
from . import views

urlpatterns = [
    #path("", views.login_home, name="auth_Index"),
    path("auth_Index/", views.login_home, name="auth_Index"),
    path("signup/", views.signup, name="signup"),
    path("signin/", views.signin, name="signin"),
    path("signout/", views.signout, name="signout"),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),

    path('', include('products.urls')),
]
