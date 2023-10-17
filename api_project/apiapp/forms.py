from django import forms
from .models import EmployeeModel

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = EmployeeModel
        fields = '__all__'

    def clean_mobile(self):
        val_mobile = self.cleaned_data.get('mobile')
        if val_mobile is not None and len(str(val_mobile)) != 10:
            raise forms.ValidationError("Mobile number must be 10 digits.")
        return val_mobile
