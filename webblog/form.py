from django import forms
from webblog.models import About,Contact,Comment,Source
from django.forms import Textarea

class AboutForm(forms.ModelForm):
    class Meta:
        model = About

    # def save(self):
        # pass

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        widgets = {
            'content': Textarea(attrs={'cols': 50, 'rows': 6}),
            }
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("author_name", "author_email", "content")
        
class SourceForm(forms.ModelForm):
    class Meta:
        model = Source
