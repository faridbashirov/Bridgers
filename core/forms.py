from django import forms
from .models import Contact, Career
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox

class ContactFormService(forms.ModelForm):
    capthca=ReCaptchaField(widget=ReCaptchaV2Checkbox())
    class Meta:
        model = Contact
        fields = ('name', 'company', 'website', 'message','capthca')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control mb-3 w-100', 'placeholder': 'Full Name'}),
            'company': forms.TextInput(attrs={'class': 'form-control mb-3 w-100', 'placeholder': 'Company Name'}),
            'website': forms.TextInput(attrs={'class': 'form-control mb-3 w-100',  'placeholder': 'Website'}),
            'message': forms.Textarea(attrs={'class': 'form-control mb-3 w-100', 'rows': '3', 'placeholder': 'Text Here'}),
        }

    
class ContactForm(forms.ModelForm):
    capthca=ReCaptchaField(widget=ReCaptchaV2Checkbox())
    class Meta:
        model = Contact
        fields = ('name', 'email', 'company', 'website', 'location', 'message','capthca')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control mb-3 w-100 py-2', 'placeholder': 'Full Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control mb-3 w-100 py-2', 'placeholder': 'Email'}),
            'company': forms.TextInput(attrs={'class': 'form-control mb-3 w-100 py-2', 'placeholder': 'Company Name'}),
            'website': forms.TextInput(attrs={'class': 'form-control mb-3 w-100 py-2',  'placeholder': 'Website'}),
            'location': forms.Select(attrs={'class': 'form-control mb-3 w-100 py-2', 'aria-label' : 'Default select example'}),
            'message': forms.Textarea(attrs={'class': 'form-control mb-3 w-100', 'rows': '3', 'placeholder': 'Text Here'}),
        }


class CareerForm(forms.ModelForm):
    class Meta:
        model = Career
        fields = ('resume',)
        widgets = {
            'resume': forms.FileInput(attrs={'class': 'form-control', 'id' : 'inputGroupFile'}),
        }
# class ConsultingForm(forms.Form):
#      capthca=ReCaptchaField(widget=ReCaptchaV2Checkbox())
     