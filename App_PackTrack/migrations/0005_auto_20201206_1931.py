# Generated by Django 3.1.2 on 2020-12-07 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_PackTrack', '0004_body_rate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='body',
            name='activity_lvl',
            field=models.FloatField(),
        ),
    ]