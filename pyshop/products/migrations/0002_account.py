# Generated by Django 3.0 on 2020-08-29 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=50)),
                ('Password', models.CharField(max_length=50)),
                ('Email', models.CharField(max_length=100)),
                ('Number', models.FloatField()),
            ],
        ),
    ]