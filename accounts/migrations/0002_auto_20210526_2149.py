# Generated by Django 3.2.3 on 2021-05-26 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='updateuser',
            name='phone',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='updateuser',
            name='phone_nok',
            field=models.CharField(max_length=50),
        ),
    ]
