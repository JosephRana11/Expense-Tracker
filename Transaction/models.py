from django.db import models
from Capital.models import Wallet

expense_choices = (
    ('Housing' , 'Housing'),
    ('Utilities' , 'Utilities'),
    ('Transportation' , 'Transportation'),
    ('Food and Beverages' , 'Food and Beverages'),
    ('Health' , 'Health'),
    ('Entertainment' , 'Entertainment'),
    ('Debt Payment' , 'Debt Payment'),
    ('Education'  , 'Education'),
    ('Miscellaneous' , 'Miscellaneous'),
)

class Expense(models.Model):
    parent_wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=12 , decimal_places=2)
    expense_type = models.CharField(max_length=50 , choices= expense_choices)
    expense_date = models.DateField(auto_now_add=True)
    expense_note = models.CharField(max_length=200 , null=True)

    def __str__(self):
        return f"{self.expense_type}-{self.amount}"

income_choices = (
    ('Salary' , 'Salary'),
    ('Commison' , 'Commison'),
    ('Debt Collection' , 'Debt Collection'),
    ('Gift' , 'Gift'),
    ('Miscellaneous' , 'Miscellaneous'),
)

class Income(models.Model):
    parent_wallet = models.ForeignKey(Wallet , on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=12 , decimal_places=2)
    income_type = models.CharField(max_length=50 , choices=income_choices)
    income_date = models.DateField(auto_now_add=True)
    income_note = models.CharField(max_length=200 , null=True)