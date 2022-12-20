from django import forms
from django.contrib.auth.models import User
from . import models

class CustomerUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }

class CustomerForm(forms.ModelForm):
    class Meta:
        model=models.Customer
        fields=['address','mobile']


class MechanicUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }

class MechanicForm(forms.ModelForm):
    class Meta:
        model=models.Mechanic
        fields=['address','mobile','skill']

class MechanicSalaryForm(forms.Form):
    salary=forms.IntegerField();


class RequestForm(forms.ModelForm):
    class Meta:
        model=models.Request
        fields=['vehicle_name','vehicle_no','problem_description']
        widgets = {
        'problem_description':forms.Textarea(attrs={'rows': 3, 'cols': 30})
        }

class AdminRequestForm(forms.Form):
    customer=forms.ModelChoiceField(queryset=models.Customer.objects.all(),empty_label="Customer Name",to_field_name='id')
    mechanic=forms.ModelChoiceField(queryset=models.Mechanic.objects.all(),empty_label="Mechanic Name",to_field_name='id')
    cost=forms.IntegerField()

class AdminApproveRequestForm(forms.Form):
    mechanic=forms.ModelChoiceField(queryset=models.Mechanic.objects.all(),empty_label="Mechanic Name",to_field_name='id')
    cost=forms.IntegerField()
    stat=(('Обрабатывается','Обрабатывается'),('Подтверждена','Подтверждена'),('Ремонт завершен','Ремонт завершен'))
    status=forms.ChoiceField( choices=stat)


class UpdateCostForm(forms.Form):
    cost=forms.IntegerField()

class MechanicUpdateStatusForm(forms.Form):
    stat=(('Подтверждена','Подтверждена'),('В ремонте','В ремонте'),('Ремонт завершен','Ремонт завершен'))
    status=forms.ChoiceField( choices=stat)

class FeedbackForm(forms.ModelForm):
    class Meta:
        model=models.Feedback
        fields=['by','message']
        widgets = {
        'message':forms.Textarea(attrs={'rows': 6, 'cols': 30})
        }

class AskDateForm(forms.Form):
    date=forms.DateField()