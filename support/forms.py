from django import forms
from .models import SupportNote

class SupportNoteForm(forms.ModelForm):
    class Meta:
        model = SupportNote
        fields = ['note']
        widgets = {
            'note': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Enter support note here...'})
        }