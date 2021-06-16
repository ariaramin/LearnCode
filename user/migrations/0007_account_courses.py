# Generated by Django 3.1.7 on 2021-06-16 08:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0024_remove_course_instructor'),
        ('user', '0006_remove_account_courses'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='courses',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='course.course'),
        ),
    ]