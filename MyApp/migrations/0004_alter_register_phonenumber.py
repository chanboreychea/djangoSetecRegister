# Generated by Django 4.2.4 on 2023-10-14 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0003_rename_emergencyemail_register_emergencyaddress_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='phoneNumber',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]