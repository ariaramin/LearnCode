# Generated by Django 3.1.6 on 2021-03-09 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('session', '0003_auto_20210307_1049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='time',
            field=models.CharField(max_length=20),
        ),
    ]
