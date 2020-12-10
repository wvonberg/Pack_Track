# Generated by Django 3.1.2 on 2020-12-09 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_PackTrack', '0014_remove_pet_pet_intact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='pet_bday',
            field=models.DateField(default='1901-01-01'),
        ),
        migrations.AlterField(
            model_name='pet',
            name='pet_carb',
            field=models.IntegerField(default=60),
        ),
        migrations.AlterField(
            model_name='pet',
            name='pet_fat',
            field=models.IntegerField(default=15),
        ),
        migrations.AlterField(
            model_name='pet',
            name='pet_goal',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='pet',
            name='pet_name',
            field=models.CharField(default='Spot', max_length=255),
        ),
        migrations.AlterField(
            model_name='pet',
            name='pet_protein',
            field=models.IntegerField(default=25),
        ),
        migrations.AlterField(
            model_name='pet',
            name='pet_weight',
            field=models.IntegerField(default=0),
        ),
    ]
