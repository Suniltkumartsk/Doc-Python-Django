from django.urls import path
from myapp import views
urlpatterns=[
    path('',views.index,name='index'),
    path('signup/',views.signup_page,name='signup'),
    path('login/',views.login_page,name='login'),
    path('home/',views.home,name='home'),
    path('register/',views.register,name='reg')
    
]