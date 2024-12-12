from django import forms

class ContactDetail(forms.Form):
    name = forms.CharField(label='Name',max_length=100)
    email = forms.EmailField(label="Email")
    message = forms.CharField(label="Message")