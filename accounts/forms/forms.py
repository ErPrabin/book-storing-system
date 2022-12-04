from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from ..models import User

class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','mobile_number','address','password1','password2']