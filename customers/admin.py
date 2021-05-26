from django.contrib import admin

from .models import CustomerAccount, Withdraw, Deposit

# Register your models here.

class CustomerAccountAdmin(admin.ModelAdmin):
  list_display = ('id', 'account_number', 'customer', 'available_bal', 'timestamp')
  list_display_links = ('id', 'account_number')
  search_fields = ('account_number',)
  list_per_page = 25

admin.site.register(CustomerAccount, CustomerAccountAdmin)

class DepositAdmin(admin.ModelAdmin):
  list_display = ('id', 'account', 'amount', 'timestamp')
  list_display_links = ('id', 'account')
  search_fields = ('account',)
  list_per_page = 25

admin.site.register(Deposit, DepositAdmin)

class WithdrawAdmin(admin.ModelAdmin):
  list_display = ('id', 'account', 'amount', 'timestamp')
  list_display_links = ('id', 'account')
  search_fields = ('account',)
  list_per_page = 25

admin.site.register(Withdraw, WithdrawAdmin)