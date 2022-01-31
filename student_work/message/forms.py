from .models import Message
from django import forms


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('user',  'text')

        widgets = {
            'user': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter your text'})
        }
