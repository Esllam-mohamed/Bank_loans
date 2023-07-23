from django.shortcuts import render,redirect
from ..models import loan,loancustomer,loanprovider,bank
from .serializers import LoanSerializer,LoanProviderSerializer
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django.contrib import messages
from rest_framework.decorators import api_view
from rest_framework.response import Response
# views.py
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
# def customer(request):
#     return render(request,r'C:\Users\Hadeer\Desktop\backend\venv\bank\templates\bank_customer.html')


def bank_provider(request):
    return render(request,r'C:\Users\Hadeer\Desktop\backend\venv\bank\templates\loan_provider.html')


def login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        if 'customer' in username:
            auth_login(request, user)
            return redirect('customer')
        elif "provider" in username :
            auth_login(request,user)
            return redirect("provider")
    else:
        messages.error(request,"Invalid username or password.")
    return render(request,r'C:\Users\Hadeer\Desktop\backend\venv\bank\templates\login.html')



class loansViewSet(viewsets.ModelViewSet):
    queryset = loan.objects.all()
    serializer_class = LoanSerializer
    permission_classes = [IsAuthenticated]

class providerViewSet(viewsets.ModelViewSet):
    queryset = loanprovider.objects.all()
    serializer_class = LoanProviderSerializer
    permission_classes = [IsAuthenticated]
    