# Generated by Django 3.1.2 on 2020-12-08 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_PackTrack', '0012_auto_20201208_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='pet_intact',
            field=models.BooleanField(),
        ),
    ]
