# Generated by Django 3.1.7 on 2021-05-19 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0003_auto_20210519_0803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(upload_to='category/image'),
        ),
    ]
