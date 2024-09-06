from django import forms
from .models import UserProfile

#form class

#model form class
class StudentRegistration(forms.ModelForm):
    class Meta:
        #(to link  model to form)
        model = UserProfile
        fields =['name','email','password']
        widgets={
            'password':forms.PasswordInput(),
        }