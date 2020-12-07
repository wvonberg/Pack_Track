# Generated by Django 3.1.2 on 2020-12-07 00:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App_PackTrack', '0002_pet_owner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bug',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issue_location', models.CharField(max_length=255)),
                ('issue_date', models.DateField()),
                ('issue_comp', models.CharField(max_length=255)),
                ('issue_desc', models.TextField()),
                ('issue_status', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_bugs', to='App_PackTrack.user')),
            ],
        ),
    ]