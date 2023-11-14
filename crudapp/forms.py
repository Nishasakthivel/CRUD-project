from django import forms
from crudapp.models import book
class bookform(forms.ModelForm):
	class Meta:
		model=book
		fields='__all__'