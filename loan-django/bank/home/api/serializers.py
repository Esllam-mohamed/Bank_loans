from rest_framework import serializers
from django.contrib.auth.models import User
from ..models import loan,loancustomer,loanprovider,bank


class LoanProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = loanprovider
        fields = ['id','name','mobile','email','password','provide_history']

class LoanCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = loancustomer
        fields = '__all__'

class BankPersonalSerializer(serializers.ModelSerializer):
    class Meta:
        model = bank
        fields = '__all__'

class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = loan
        fields = ['loan_amoount',' duration','interest_rate','total_loan','minimum_salar']