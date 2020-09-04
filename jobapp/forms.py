from django import forms

from .models import Job_Details

class Job_DetailsForm(forms.ModelForm):

    class Meta:
        model = Job_Details
        fields = '__all__'
