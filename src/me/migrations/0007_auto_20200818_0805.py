# Generated by Django 3.0.8 on 2020-08-18 08:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('me', '0006_accountmodel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='accountmodel',
            old_name='coursePublisher',
            new_name='about',
        ),
    ]
