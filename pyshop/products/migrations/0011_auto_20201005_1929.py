# Generated by Django 3.0 on 2020-10-05 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_auto_20200927_1220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='icon',
            field=models.ImageField(upload_to='media/profileicons'),
        ),
    ]