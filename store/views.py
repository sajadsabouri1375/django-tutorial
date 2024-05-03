from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F
from django.db.models.aggregates import Count, Max, Min, Avg
from django.db.models import Value
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
        
    customers = Customer.objects.filter(first_name__startswith=F('last_name'))
    for customer in customers:
        print(f'{customer.first_name}-{customer.last_name}')
    
    customers = Customer.objects.order_by('first_name', '-last_name')
    for customer in customers:
        print(f'{customer.first_name}-{customer.last_name}')
    
    result = Customer.objects.aggregate(count=Count('id'), min_id=Min('id'))
    print(result)
    
    customers = Customer.objects.annotate(is_new=Value(True))
    for customer in customers:
        print(customer.is_new)
        
    return render(request, 'hello.html', {'customers': list(customers)})
