# Generated by Django 3.1.6 on 2021-03-11 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('session', '0008_auto_20210311_1249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='video',
            field=models.FileField(upload_to='static/session/videos'),
        ),
    ]
