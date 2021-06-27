from django.conf import settings
from django.db import models
from django.utils import timezone
from django import forms


class Submission(models.Model):
    GENDER = (
        ('Pene', 'Pene'),
        ('Vagina', 'Vagina'),
        ('Rettile', 'Rettile'),
    )
    age = models.PositiveIntegerField(default=1)
    gender = models.CharField(max_length=200, choices=GENDER)
    text = models.TextField(widget=forms.Textarea)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.pk)
