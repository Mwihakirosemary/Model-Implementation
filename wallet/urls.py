# from unicodedata import name
from django.urls import path
from . import views
# from .views import account_details, card_details, customer_reward, loan_details, notify_customer, recieve_reciept, register_customer, third_party_details, transaction_details, wallet_information

urlpatterns = [
    path("register/",views.register_customer, name ="registration"),
    path("wallet/",views.wallet_information, name = "wallet"),
    path("account/",views.account_details, name= "account"),
    path("transaction/",views.transaction_details, name= "transaction"),
    path("card/",views.card_details, name= "card"),
    path("thirdparty/",views.third_party_details, name= "thidparty"),
    path("notify/",views.notify_customer, name= "notifications"),
    path("reciept/",views.recieve_reciept, name= "reciept"),
    path("loan/",views.loan_details, name= "loan"),
    path("reward/",views.customer_reward, name= "reward"),
    path("customers/",views.list_customers, name= "customers_list"),
    path("wallet_info/",views.list_wallet_information, name= "list_information"),
    path("accounts/",views.list_accounts, name= "list_accounts"),
    path("transactions/",views.list_transactions, name= "list_transactions"),
    path("cards/",views.list_cards, name= "list_cards"),
    path("thirdparty_det/",views.list_third_party, name= "third_party"),
    path("notifications/",views.list_notifications, name= "list_notfcs"),
    path("customer_det/",views.list_reciepts, name= "details_list"),
    path("loans/",views.list_loans, name= "cust_loans"),
    path("rewards/",views.list_reward, name= "rewards_list"),
]