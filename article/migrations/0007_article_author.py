# Generated by Django 3.1.7 on 2021-06-14 14:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_account_is_instructor'),
        ('article', '0006_auto_20210519_0811'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.account'),
        ),
    ]