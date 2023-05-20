from django.urls import path,include
from . import views

urlpatterns = [
    path('members/', views.members, name='members')
]
