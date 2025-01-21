
from django.urls import path
from .views import aboutpage,delivarypage,foodpage
urlpatterns = [
    path(' ',foodpage,name='home'),
    path('about/<int:id>/',aboutpage,name='about'),
    path('delivarys/',delivarypage),
]