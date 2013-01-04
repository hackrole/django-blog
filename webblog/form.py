from django import forms
from webblog.models import About,Contact

class AboutForm(forms.ModelForm):
    class Meta:
        model = About

    # def save(self):
        # pass

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        
    
