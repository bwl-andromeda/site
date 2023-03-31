from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('signup',views.signup,name='signup'),
    path('logging',views.login_view,name="logging"),
    path('logout',views.logout_view,name='logout'),
    ]
