# Generated by Django 3.1.6 on 2021-03-09 15:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('session', '0006_auto_20210309_1814'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='session',
            name='status',
        ),
    ]