# forms.py

from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'email', 'mobile', 'gender', 'designation', 'course', 'profile_image']
        widgets = {
            'gender': forms.RadioSelect
            
        }
