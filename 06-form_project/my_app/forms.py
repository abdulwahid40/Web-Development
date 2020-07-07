# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 12:12:06 2020

@author: Abdul Wahid
"""


from django import forms
#from django.core import validators

# def check_for_z(value):
#     if value[0].lower() != 'z':
#         raise forms.ValidationError("Need to start with Z")
# validators = [check_for_z]



class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label = "Enter email again: ")
    text = forms.CharField(widget = forms.Textarea)

    
    def clean(self):
        all_clean_data = super().clean()
        emailp = all_clean_data['email']
        vemail = all_clean_data['verify_email']
    
        if emailp != vemail:
            raise forms.ValidationError("Emails not matched")