# Generated by Django 3.0 on 2020-09-27 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20200926_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='icon',
            field=models.FileField(default='default_icon.png', upload_to=''),
        ),
    ]
