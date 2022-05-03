from django.urls import path, include
from .Controllers.HomeController import HomeController
from . Controllers.UserController import UserController
from . Controllers.LoginController import LoginController
from django.conf.urls import handler404


urlpatterns = [
    path('', LoginController.login, name='loginIAM'),
    path('home', HomeController.home, name='homeIAM'),
    path('about', HomeController.about, name='aboutIAM'),
    path('login', LoginController.login, name='loginIAM'),
    path('validate', LoginController.loginPost, name = 'validate'),
    path('logout', LoginController.logout, name = 'logout'),

]