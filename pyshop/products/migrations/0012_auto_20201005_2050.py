# Generated by Django 3.0 on 2020-10-05 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_auto_20201005_1929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='icon',
            field=models.ImageField(upload_to='profileicons'),
        ),
    ]
