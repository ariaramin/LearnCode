# Generated by Django 3.1.7 on 2021-06-16 07:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_account_is_instructor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='is_instructor',
        ),
    ]
