from django.urls import path
from .views import home_view , login_view , register_view , logout_view
from .views import test_view

urlpatterns = [
    path('' , home_view , name='home'),
    path('login/' , login_view , name='login'),
    path('register' , register_view , name = 'register'),
    path('test/' , test_view),
    path('logout/' , login_view , name='logout'),
]
