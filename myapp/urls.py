from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup_page, name='signup'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('home/', views.home, name='home'),
    path('register/', views.register, name='reg'),
    path('my-appointments/', views.my_appointments, name='appointments'),
]
