# Generated by Django 3.1.7 on 2021-06-16 08:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_remove_account_is_instructor'),
        ('course', '0018_auto_20210616_0818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='instructor',
            field=models.OneToOneField(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.account'),
        ),
    ]