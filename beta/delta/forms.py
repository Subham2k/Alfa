from django import forms
from .models import Tenants


class TenantCreateForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'id':'c-name'}));
    age = forms.CharField(widget=forms.TextInput(attrs={'id':'c-age','type':'number'}));
    gender = forms.CharField(widget=forms.TextInput(attrs={'id':'c-gender'}));
    mobileno_1 = forms.CharField(widget=forms.TextInput(attrs={'id':'c-num1','type':'number'}));
    mobileno_2 = forms.CharField(widget=forms.TextInput(attrs={'id':'c-num2','type':'number'}));
    mobileno_3 = forms.CharField(widget=forms.TextInput(attrs={'id':'c-num3','type':'number'}));
    address = forms.CharField(widget=forms.Textarea(attrs={'id':'c-address'}));
    city = forms.CharField(widget=forms.TextInput(attrs={'id':'c-city'}));
    country = forms.CharField(widget=forms.TextInput(attrs={'id':'c-country'}));

    class Meta:
        model = Tenants
        fields = ['name','age','gender','mobileno_1','mobileno_2','mobileno_3','address','city','country','location']


class TenantUpdateForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'id':'e-name'}));
    age = forms.CharField(widget=forms.TextInput(attrs={'id':'e-age','type':'number'}));
    gender = forms.CharField(widget=forms.TextInput(attrs={'id':'e-gender'}));
    mobileno_1 = forms.CharField(widget=forms.TextInput(attrs={'id':'e-num1','type':'number'}));
    mobileno_2 = forms.CharField(widget=forms.TextInput(attrs={'id':'e-num2','type':'number'}));
    mobileno_3 = forms.CharField(widget=forms.TextInput(attrs={'id':'e-num3','type':'number'}));
    address = forms.CharField(widget=forms.Textarea(attrs={'id':'e-address'}));
    city = forms.CharField(widget=forms.TextInput(attrs={'id':'e-city'}));
    country = forms.CharField(widget=forms.TextInput(attrs={'id':'e-country'}));

    class Meta:
        model = Tenants
        fields = ['name','age','gender','mobileno_1','mobileno_2','mobileno_3','address','city','country','location']