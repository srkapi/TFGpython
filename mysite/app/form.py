from  models import *
from django import forms

from app.models import Users


class UserForm(forms.ModelForm):
      class Meta:
            model = Users
            fields = ('name', 'last_name', 'user', 'password' , 'email' , 'active' )