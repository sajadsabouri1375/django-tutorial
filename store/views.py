from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F
from django.db.models.aggregates import Count, Max, Min, Avg
from django.db.models import Value
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import CustomerSerializer
from .models import Customer


@api_view()
def customers_list(request):
    queryset = Customer.objects.all()
    serializer = CustomerSerializer(queryset, many=True)
    return Response(serializer.data)

@api_view()
def customer_details(request, id):
    
    # try:
    #     customer = Customer.objects.get(pk=id)
    #     serializer = CustomerSerializer(customer)
    #     return Response(serializer.data)
    # except Customer.DoesNotExist:
    #     return Response(status=status.HTTP_404_NOT_FOUND)
    
    # Instead, we could:
    customer = get_object_or_404(Customer, pk=id)
    serializer = CustomerSerializer(customer)
    return Response(serializer.data)

    
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
