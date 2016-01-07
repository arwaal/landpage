from django import forms
from django.forms import extras 
from django.forms.fields import Field
from django.contrib.auth.models import User
from django.core import exceptions
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.forms import ValidationError
from main.models import Users, Landpage
import re
from datetime import date


class KuwaitiMobile(forms.Field):
    def validate(self, value):
        if value != "":
            kuwait_mobile = re.compile('^(9|6|5)(\d{7})$')
            mobile_match = kuwait_mobile.match(value)
            if mobile_match == None:
                raise exceptions.ValidationError(('Invalid Number: %(value)s'),
                    code='invalied',
                    params={'value': 'Please enter a valid Kuwaiti Mobile number'},
                    )
            else:
                return value
        else:
            return value


class UserSignup(forms.Form):
    first_name = forms.CharField(max_length=255, required=True)
    last_name = forms.CharField(max_length=255, required=True)
    mobile = KuwaitiMobile(required=True, help_text='enter your 8 digits number')
    # gender = forms.ChoiceField(choices=Users.GENDER_TYPE, required=True)
    # date_of_birth = forms.DateField(widget=extras.SelectDateWidget(years=range(2000,1920,-1)), required=True)
    # password = forms.CharField(widget=forms.PasswordInput(), required=True)
    email = forms.CharField(max_length=255, required=True)







