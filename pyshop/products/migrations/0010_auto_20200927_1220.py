# Generated by Django 3.0 on 2020-09-27 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_auto_20200927_1115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='icon',
            field=models.ImageField(upload_to=''),
        ),
    ]
