# Generated by Django 3.1.2 on 2020-12-08 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_PackTrack', '0010_remove_pet_profile_validate'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='pet_rate',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]