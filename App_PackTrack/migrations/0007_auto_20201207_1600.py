# Generated by Django 3.1.2 on 2020-12-08 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_PackTrack', '0006_auto_20201207_1432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='pet_intact',
            field=models.CharField(max_length=20),
        ),
    ]