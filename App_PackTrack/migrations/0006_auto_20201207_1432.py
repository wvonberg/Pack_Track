# Generated by Django 3.1.2 on 2020-12-07 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_PackTrack', '0005_auto_20201206_1931'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='pet_carb',
            field=models.IntegerField(default=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pet',
            name='pet_fat',
            field=models.IntegerField(default=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pet',
            name='pet_protein',
            field=models.IntegerField(default=40),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pet',
            name='pet_act_lvl',
            field=models.FloatField(max_length=48),
        ),
    ]