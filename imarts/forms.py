from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
#from phonenumber_field.modelfields import PhoneNumberField
class SearchForm(forms.Form):
	search_item = forms.CharField(
		label='Search here',
		max_length=50,
		help_text='Enter product to search'
	)

	class Meta:
		model = User
		fields = ('search_item', )
		widgets = {
			'search_item': forms.TextInput(),
		}


class BuyForm(forms.Form):
	cnf_item = forms.CharField(
		label='ConfirmName',
		max_length=50,
	)
	use_name = forms.CharField(
		label='Your Name',
		max_length=50,
	)
	address = forms.CharField(
		label='Full Address',
		max_length=50,
	)

	class Meta:
		model = User
		fields = ('cnf_item','use_name','address', )
		widgets = {
			'cnf_item': forms.TextInput(),
			'use_name': forms.TextInput(),
			'address': forms.TextInput(),
		}


class CatForm(forms.Form):
	cat_item = forms.CharField(
		label='Category',
		max_length=50,
	)

	class Meta:
		model = User
		fields = ('cat_item', )
		widgets = {
			'cat_item': forms.TextInput(),
		}