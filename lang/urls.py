from django.urls import path

from . import views

app_name = 'lang'

urlpatterns = [
    path('', views.home, name='home'),
    path('item/', views.item, name='item'),
]