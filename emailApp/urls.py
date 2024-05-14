from . import views
from django.urls import path

urlpatterns =[
 path('form', views.get_name, name='form')
]