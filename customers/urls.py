from django.urls import path


from .views import CustomerAccountList, DepositList, WithdrawList

urlpatterns = [
    path('api/customersaccountlist/', CustomerAccountList.as_view()),
    path('api/depositList/', DepositList.as_view()),
    path('api/withdrawList/', WithdrawList.as_view()),
]

