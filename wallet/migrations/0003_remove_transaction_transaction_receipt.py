# Generated by Django 4.0.6 on 2022-08-01 19:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0002_remove_wallet_transaction_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='transaction_receipt',
        ),
    ]
