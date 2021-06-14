from django.urls import path


from .views import CustomerAccountList, DepositList, WithdrawList, TransferList

urlpatterns = [
    path('api/customersaccountlist/', CustomerAccountList.as_view()),
    path('api/depositList/', DepositList.as_view()),
    path('api/withdrawList/', WithdrawList.as_view()),
    path('api/TransferList/', TransferList.as_view()),
]

