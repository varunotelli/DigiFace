#from .models import Person
from django import forms

class Userform(forms.ModelForm):
	#password=forms.CharField(widget=forms.PasswordInput)
    #template_name=''
	class Meta:
		#model=Person
		fields=['Name','DOB','Street','Locality','City','District','State','Pincode','UID']