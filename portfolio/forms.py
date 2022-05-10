from django import forms
from .models import UserContact


class UserContactForm(forms.ModelForm):

	name = forms.CharField(max_length=100, required=True,
		widget=forms.TextInput(attrs={
			'placeholder': 'Your Name',
			
			}))

	email = forms.EmailField(max_length=254, required=True, 
		widget=forms.TextInput(attrs={
			'placeholder': 'Your Email',
			
			}))


	phone = forms.CharField(max_length=20, required=True, 
		widget=forms.TextInput(attrs={
			'placeholder': 'Your Number',
			
			}))

	subject = forms.CharField(max_length=200, required=True, 
		widget=forms.TextInput(attrs={
			'placeholder': 'Subject',
			
			}))
			
	message = forms.CharField(max_length=1000, required=True, 
		widget=forms.Textarea(attrs={
			'placeholder': 'Type Your Message Here',
			'rows': 6,
			}))


	class Meta:
		model = UserContact
		fields = ('name', 'email', 'phone', 'subject', 'message',)