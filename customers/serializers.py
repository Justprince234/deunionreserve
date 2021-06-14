from rest_framework import serializers

from .models import CustomerAccount, Withdraw, Deposit, Transfer

class CustomerAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerAccount
        fields = '__all__'

class WithdrawSerializer(serializers.ModelSerializer):
    class Meta:
        model = Withdraw
        fields = '__all__'

class DepositSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deposit
        fields = '__all__'

class TransferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transfer
        fields = '__all__'