# Generated by Django 3.1.7 on 2021-06-16 08:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_remove_account_is_instructor'),
        ('course', '0017_auto_20210616_0817'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='instructor',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.account'),
        ),
    ]