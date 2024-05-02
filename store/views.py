from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from .models import Customer


def work_with_data(request):
    
    # Get a customer
    try:
        customer = Customer.objects.get(id = 0)
        print(customer)
    except ObjectDoesNotExist:
        print(f'The requests ID does not exist.')
        pass
    
    customer = Customer.objects.get(first_name = 'Kendricks')
    print(customer.first_name)
    
    customers = Customer.objects.filter(first_name__in = ['Kendricks', 'Flori'], first_name__startswith='K')
    for customer in customers:
        print(customer.first_name)
    
    customers = Customer.objects.filter(Q(first_name__in = ['Kendrics']) | Q(first_name__startswith='F'))
    for customer in customers:
        print(customer.first_name)
        
    return render(request, 'hello.html')
