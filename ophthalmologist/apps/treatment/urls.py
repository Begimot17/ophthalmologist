from django.urls import path
from . import views

app_name = 'treatment'

urlpatterns = [
    path('',views.index, name='index'),
]
