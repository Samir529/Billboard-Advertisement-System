# Generated by Django 2.2.17 on 2021-07-27 18:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Billboard_Advertisement', '0004_remove_customerprofileinfo_password'),
    ]

    operations = [
        migrations.RenameField(
            model_name='advertiserprofileinfo',
            old_name='Advertiser_profile_pic',
            new_name='profile_picture',
        ),
        migrations.RenameField(
            model_name='citycorporationprofileinfo',
            old_name='cityCor_profile_pic',
            new_name='profile_picture',
        ),
        migrations.RenameField(
            model_name='customerprofileinfo',
            old_name='Customer_profile_pic',
            new_name='profile_picture',
        ),
    ]
