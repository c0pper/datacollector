# Generated by Django 2.2.24 on 2021-06-13 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collector', '0002_auto_20210613_1337'),
    ]

    operations = [
        migrations.AddField(
            model_name='submission',
            name='age',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
    ]