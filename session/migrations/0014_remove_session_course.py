# Generated by Django 3.1.7 on 2021-06-14 12:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('session', '0013_remove_session_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='session',
            name='course',
        ),
    ]
