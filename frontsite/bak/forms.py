# coding: UTF-8

from __future__ import unicode_literals

from django.core.exceptions import ValidationError
from django.forms import ModelForm

from .models import User


class UserForm(ModelForm):
    class Meta:
        model=User
        fields='__all__'

    def clean_name(self):
        username = self.cleaned_data.get('name')
        if username == "xieyaxiong":
            raise ValidationError(u'%s被使用了，请换个名字!' % username)
        else:
            return username