# Generated by Django 4.2.2 on 2023-08-19 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlineapp', '0003_alter_userprofile_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_picture',
            field=models.ImageField(upload_to='profile_pic/'),
        ),
    ]