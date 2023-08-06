from django import forms


class OrderForm(forms.Form):
    name = forms.CharField(max_length=100, required=False)
    phone = forms.CharField(max_length=12)