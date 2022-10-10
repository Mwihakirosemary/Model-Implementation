from django.shortcuts import render
from wallet.models import *
from . import serializer
from rest_framework import viewsets


# Create your views here.
class CustomerViewSet(viewsets.ModelViewSet):
    queryset=Customer.objects.all()
    serializer_class=serializer.CustomerSerializer

class WalletViewSet(viewsets.ModelViewSet):
    queryset=Wallet.objects.all()
    serializer_class=serializer.WalletSerializer

class AccountViewSet(viewsets.ModelViewSet):
        queryset=Account.objects.all()
        serializer_class=serializer.AccountSerializer

class CardViewSet(viewsets.ModelViewSet):
    queryset=Card.objects.all()
    serializer_class=serializer.CardSerializer

class TransactionViewSet(viewsets.ModelViewSet):
    queryset=Transaction.objects.all()
    serializer_class=serializer.TransactionSerializer

class LoanViewSet(viewsets.ModelViewSet):
    queryset=Loan.objects.all()
    serializer_class=serializer.LoanSerializer

class ReceiptViewSet(viewsets.ModelViewSet):
        queryset=Receipt.objects.all()
        serializer_class=serializer.RecieptSerializer

class NotificationsViewSet(viewsets.ModelViewSet):
        queryset=Notifications.objects.all()
        serializer_class=serializer.NotificationsSerializer

