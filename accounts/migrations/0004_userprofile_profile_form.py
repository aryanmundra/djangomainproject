# Generated by Django 3.2 on 2021-07-02 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='profile_form',
            field=models.ImageField(blank=True, upload_to='images/users/'),
        ),
    ]
