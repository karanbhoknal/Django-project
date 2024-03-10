from django import forms
from .models import BasicModel, GeeksModel, RegisterModel


class GeeksForm(forms.ModelForm):
 
    # create meta class 
    class Meta:
        # specify model to be used
        model = GeeksModel
 
        # specify fields to be used
        fields = [
            "title",
            "description",
        ]



# creating a register form
class RegisterForm(forms.ModelForm):
 
    # create meta class
    class Meta:
        # specify model to be used
        model = RegisterModel
 
        # specify fields to be used
        fields = [
            "firstname",
            "lastname",
            "email",
            "contactnumber",
            "password",
            "confirmpassword",
            "description",
        ]

# creating a login form
class LoginForm(forms.ModelForm):
 
    # create meta class
    class Meta:
        # specify model to be used
        model = RegisterModel
 
        # specify fields to be used
        fields = [
            "email",
            "password",
        ]
        
# creating a form
class BasicForm(forms.ModelForm):
 
    # create meta class
    class Meta:
        # specify model to be used
        model = BasicModel
 
        # specify fields to be used
        fields = [
            "title",
            "description",
        ]
