from django.urls import path
from . import views

urlpatterns = [
    path('data/', views.work_with_data)
]