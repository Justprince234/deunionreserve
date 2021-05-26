from django.db import models

from accounts.models import UpdateUser

# Create your models here.

class CustomerAccount(models.Model):
       account_number = models.PositiveIntegerField(unique=True)
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