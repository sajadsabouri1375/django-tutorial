from django.urls import path
from . import views

urlpatterns = [
    path('data/', views.work_with_data),
    path('customers/', views.customers_list),
    path('customers/<int:id>/', views.customer_details)
]