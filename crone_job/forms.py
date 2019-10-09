"""
Basic Django forms for simple create new user
Help with DB and security
"""

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


# Custom class extend from Django forms
class SignUpForm(UserCreationForm):
	email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}))
	first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
	last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

	# Changes exist class User in models
	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

	# Added classes for Django forms elements with help_text
	def __init__(self, *args, **kwargs):
		super(SignUpForm, self).__init__(*args, **kwargs)
		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['username'].help_text = ''
		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].help_text = ''
		self.fields['password2'].widget.attrs['class'] = 'form-control mb-5'
		self.fields['password2'].help_text = ''
