from django.urls import path
from . import views

app_name = 'treatment'

urlpatterns = [
    path('',views.index, name='index'),
    path('update/<int:id>', views.update, name='update'),
    path('upd/<int:id>', views.upd, name='upd'),
    path('delete/<int:id>', views.delete, name='delete'),
]
