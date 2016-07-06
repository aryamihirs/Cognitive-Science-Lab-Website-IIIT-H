from django import forms 

#form to act as search field.
class NameForm(forms.Form):
	search_for = forms.CharField(label='Search Posts', max_length=200)
