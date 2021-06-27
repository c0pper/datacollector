from django import forms
from django.forms import Textarea
from .models import Submission


class SubmissionForm(forms.ModelForm):

    class Meta:
        model = Submission
        fields = ('age', 'gender', 'text',)
        widgets = {
            'text': Textarea(attrs={'cols': 25, 'rows': 10}),
        }
