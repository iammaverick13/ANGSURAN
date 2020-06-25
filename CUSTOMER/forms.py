from django import forms

class AdminForm(forms.Form):
	username = forms.CharField(max_length=100)
	password = forms.CharField(max_length=255, widget=forms.PasswordInput)

class CustomerForm(forms.Form):
	username = forms.CharField(max_length=100)
	jumlah_utang = forms.IntegerField()

class UpdateUtang(forms.Form):
	jumlah_bayar = forms.IntegerField()