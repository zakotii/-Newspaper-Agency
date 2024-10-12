from django import forms
from .models import Newspaper

class NewspaperForm(forms.ModelForm):
    class Meta:
        model = Newspaper
        fields = ['title', 'content', 'published_date', 'publication_date', 'topic', 'redactor', 'publishers']
