from __future__ import unicode_literals

from django.db import models
from django.forms import ModelForm
from .models import User


class UserForm(ModelForm):
    class Meta:
        model=User
        fields='__all__'
