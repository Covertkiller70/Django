from django import forms
from django.core import validators
from applvl3.models import User

class MyForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    verifyemail = forms.EmailField(label='Enter your email again')
    text = forms.CharField(widget=forms.Textarea)
    botcatch = forms.CharField(required=False, widget=forms.HiddenInput)

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verifyemail']
        if email != vmail:
            raise forms.ValidationError('Emails do not match!')

class LandForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
    

