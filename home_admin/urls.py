from django.urls import path
from home_admin.views import home;

urlpatterns = [
    
    path('',home)
]