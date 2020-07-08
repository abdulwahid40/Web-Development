# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 23:35:29 2020

@author: Abdul Wahid
"""


from django import forms
from appTwo.models import User

class NewUserForm(forms.ModelForm):
    
    class Meta():
        model = User
        fields = "__all__"
        
        
        
        