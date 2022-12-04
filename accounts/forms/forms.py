from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from ..models import CustomUser

class CreateUserForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'required':'',
            'name':'username',
            'placeholder':'UserName',
        })
        self.fields['first_name'].widget.attrs.update({
            'required':'',
            'name':'first_name',
            'placeholder':'Firstname',
        })
        self.fields['last_name'].widget.attrs.update({
            'required':'',
            'name':'last_name',
            'placeholder':'Lastname',
        })
        self.fields['email'].widget.attrs.update({
            'required':'',
            'name':'email',
            'type':'email',
            'placeholder':'Email',
        })
        self.fields['mobile_number'].widget.attrs.update({
            'required':'',
            'name':'mobile_number',
            'placeholder':'Mobile Number',
        })
        self.fields['address'].widget.attrs.update({
            'required':'',
            'name':'address',
            'placeholder':'Address',
        })
        self.fields['password1'].widget.attrs.update({
            'required':'',
            'name':'password1',
            'type':'password',
            'placeholder':'Password',
        })
        self.fields['password2'].widget.attrs.update({
            'required':'',
            'name':'password2',
            'type':'password',
            'placeholder':'Password Again',
        })
    class Meta:
        model=CustomUser
        fields=['username','email','mobile_number','address','password1','password2','first_name','last_name']