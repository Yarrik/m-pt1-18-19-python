from django.urls import path

from . import views

urlpatterns = [
    path('contacts/', views.cont, name='cont'),
    path('', views.index, name='index')
]