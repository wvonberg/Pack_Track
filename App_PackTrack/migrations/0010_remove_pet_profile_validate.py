# Generated by Django 3.1.2 on 2020-12-08 20:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App_PackTrack', '0009_pet_profile_validate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pet',
            name='profile_validate',
        ),
    ]