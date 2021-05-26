from django.shortcuts import render

from rest_framework import generics

from .models import CustomerAccount, Withdraw, Deposit
from .serializers import CustomerAccountSerializer, DepositSerializer, WithdrawSerializer

# Create your views here.

class CustomerAccountList(generics.ListCreateAPIView):
    queryset = CustomerAccount.objects.all()
    serializer_class = CustomerAccountSerializer

class WithdrawList(generics.ListCreateAPIView):
    queryset = Withdraw.objects.all()
    serializer_class = WithdrawSerializer

class DepositList(generics.ListCreateAPIView):
    queryset = Deposit.objects.all()
    serializer_class = DepositSerializer