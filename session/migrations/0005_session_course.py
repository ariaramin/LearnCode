# Generated by Django 3.1.6 on 2021-03-09 14:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_auto_20210309_1814'),
        ('session', '0004_auto_20210309_1808'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='course',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='course.course'),
        ),
    ]
