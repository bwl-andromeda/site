from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('register/',views.signup,name='register'),
    path('vhod',views.login_view,name="vhod"),
    path('logout',views.logout_view,name='logout'),
]
