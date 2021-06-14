from django.db import models

import random

from accounts.models import UpdateUser

# Create your models here.
def random_account():
       return str(random.randint(1000000000, 10000000000))

class CustomerAccount(models.Model):
       account_number = models.CharField(default=random_account, unique=True, max_length=200)
       customer =models.OneToOneField(UpdateUser, related_name='user',on_delete=models.CASCADE)
       available_bal = models.DecimalField(default=0, max_digits=12, decimal_places=2)
       timestamp = models.DateTimeField(auto_now_add=True)

       class Meta:
              verbose_name_plural = "Customer Data"
  
       def __str__(self):
              return "{}".format(self.account_number)

class Withdraw(models.Model):
       amount = models.FloatField()
       account = models.ForeignKey(CustomerAccount, on_delete=models.CASCADE)
       timestamp = models.DateTimeField(auto_now_add=True)

       class Meta:
              verbose_name_plural = "Customer Withdrawals"

       def __str__(self):
              return "Withdrawal of {} was made from {}".format(self.amount, self.account)

class Deposit(models.Model):
       amount = models.FloatField()
       account = models.ForeignKey(CustomerAccount, on_delete=models.CASCADE)
       timestamp = models.DateTimeField(auto_now_add=True)

       class Meta:
              verbose_name_plural = "Customer Deposits"

       def __str__(self):
              return "Deposit of {} was made to {}".format(self.amount, self.account)

class Transfer(models.Model):
       account_owner = models.OneToOneField(UpdateUser, related_name='owner',on_delete=models.CASCADE)
       from_account = models.CharField(max_length=200)
       to_account = models.CharField(max_length=200)
       amount = models.FloatField()
       timestamp = models.DateTimeField(auto_now_add=True)

       class Meta:
              verbose_name_plural = "Customer Transfers"

       def __str__(self):
              return "{} was tranfered to {} from {}".format(self.amount, self.to_account, self.from_account)