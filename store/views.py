from django.shortcuts import render
from .models import Customer


def work_with_data(request):
    customers = Customer.objects.all()
    
    for customer in customers:
        print(customer.given_name)
        
    return render(request, 'hello.html')
