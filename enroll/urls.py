from django.urls import path
from . import views
urlpatterns = [
    path('login/',views.user_login),
    path('registration/',views.showformdata , name='registration'),
    path('profile/',views.user_profile, name='profile'),
    
]
