from django.conf import settings
from django.db import models
from django.utils import timezone


class Submission(models.Model):
    GENDER = (
        ('Pene', 'Pene'),
        ('Vagina', 'Vagina'),
    )
    age = models.PositiveIntegerField(default=1)
    gender = models.CharField(max_length=200, choices=GENDER)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.pk
