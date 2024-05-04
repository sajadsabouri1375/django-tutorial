from rest_framework import serializers
from .models import Customer

class CustomerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Customer
        fields = ['id', 'first_name', 'last_name', 'date_of_birth', 'is_legal']
        
    # id = serializers.IntegerField()
    # first_name = serializers.CharField(max_length=255)
    # last_name = serializers.CharField(max_length=255)
    date_of_birth = serializers.DateField(source='birth_date')
    is_legal = serializers.SerializerMethodField(method_name='is_under_18')
    
    def is_under_18(self, customer: Customer):
        return customer.birth_date