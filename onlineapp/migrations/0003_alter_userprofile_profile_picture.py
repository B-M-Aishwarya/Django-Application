# Generated by Django 4.2.2 on 2023-08-19 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlineapp', '0002_rename_user_userprofile_alter_doctor_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pic/'),
        ),
    ]
