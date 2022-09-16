from django.shortcuts import render
from . import forms
# Create your views here.

def register_customer(request):  #1
    from .forms import CustomerRegistrationForm
    if request.method == 'POST':
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
    else:
        form = CustomerRegistrationForm()
    return render(request,"wallet/register_customer.html",{"form": form})

def list_customers(request):
    customers = forms.Customer.objects.all()
    return render(request,"wallet/list_customers.html",{"customers":customers})


def wallet_information(request):   #2
    if request.method == 'POST':
        form = forms.WalletInformation()
        if form.is_valid():
            user = form.save()
    else:
        form = forms.WalletInformation()
    return render(request,"wallet/wallet_information.html",{"form":form})

def list_wallet_information(request):
    wallets = forms.Wallet.objects.all()
    return render(request,"wallet/list_wallet_information.html",{"wallets":wallets})


def account_details(request):   #3
    if request.method == 'POST':
        form = forms.AccountDetails()
        if form.is_valid():
            user = form.save()
    else:
        form = forms.AccountDetails()
    return render(request,"wallet/account_details.html",{"form":form})

def list_accounts(request):
    accounts = forms.Account.objects.all()
    return render(request,"wallet/list_accounts.html",{"accounts":accounts})


def transaction_details(request):  #4
    if request.method == 'POST':
        form = forms.TransactionDetails()
        if form.is_valid():
            user = form.save()
    else:
        form = forms.TransactionDetails()
    return render(request,"wallet/transaction_details.html",{"form":form})

def list_transactions(request):
    transactions = forms.Transaction.objects.all()
    return render(request,"wallet/list_transactions.html",{"transactions":transactions})


def card_details(request):  #5
    if request.method == 'POST':
        form = forms.CustomerCardDetails()
        if form.is_valid():
            user = form.save()
    else:
        form = forms.CustomerCardDetails()
    return render(request,"wallet/card_details.html",{"form":form})

def list_cards(request):
    cards = forms.Card.objects.all()
    return render(request,"wallet/list_cards.html",{"cards":cards})


def third_party_details(request):   #6
    if request.method == "POST":
        form = forms.ThirdPartyDetails()
        if form.is_valid():
            user = form.save()
    else:
        form = forms.ThirdPartyDetails()
    return render(request,"wallet/third_party_details.html",{"form":form})

def list_third_party(request): 
    third_parties = forms.ThirdParty.objects.all()
    return render(request,"wallet/list_third_party.html",{"third_parties":third_parties})

def notify_customer(request):  #7
    if request.method == "POST":
        form = forms.CustomerNotifications()
        if form.is_valid():
            user = form.save()
    else:
        form = forms.CustomerNotifications()
    return render(request,"wallet/notify_customer.html",{"form":form})

def list_notifications(request):
    notification = forms.Notifications.objects.all()
    return render(request,"wallet/list_notifications.html",{"notifications":notification})

def recieve_reciept(request):   #8
    if request.method == "POST":
        form = forms.TransactionReciept()
        if form.is_valid():
            user = form.save()
    else:
        form = forms.TransactionReciept()
    return render(request,"wallet/recieve_reciept.html",{"form":form})

def list_reciepts(request):
    reciepts = forms.Receipt.objects.all()
    return render(request,"wallet/list_reciepts.html",{"reciepts":reciepts})



def loan_details(request):  #9
    if request.method == "POST":
        form = forms.LoanDetails()
        if form.is_valid():
            user = form.save()
    else:
        form = forms.LoanDetails()
    return render(request,"wallet/loan_details.html",{"form":form})

def list_loans(request):
    loans = forms.Loan.objects.all()
    return render(request,"wallet/list_loans.html",{"loans":loans})


def customer_reward(request):   #10
    if request.method == "POST":
        form = forms.CustomerReward()
        if form.is_valid():
            form.save()
    else:
        form = forms.CustomerReward()
    return render(request,"wallet/customer_reward.html",{"form":form})

def list_reward(request):
    rewards = forms.Reward.objects.all()
    return render(request,"wallet/list_reward.html",{"rewards":rewards})
