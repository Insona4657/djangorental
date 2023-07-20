# Generated by Django 4.2.3 on 2023-07-20 06:24

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('djangorental', '0016_alter_userprofile_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='address',
            field=models.CharField(default='update your address here', max_length=100),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='number',
            field=phonenumber_field.modelfields.PhoneNumberField(default='update your contact here', max_length=128, region=None),
        ),
    ]
