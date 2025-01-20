from django.urls import path,include
from .views import indexpage
urlpatterns = [
    
    path('',indexpage),
]