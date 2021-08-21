# Generated by Django 3.2.5 on 2021-07-23 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Billboard_Advertisement', '0016_alter_post_advertise_table_posted_billboards_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertiserprofileinfo',
            name='Advertiser_profile_pic',
            field=models.ImageField(blank=True, default='/profiles_pic/Advertiser_profile_pic/demo_profile_pic2.png', upload_to='profiles_pic/Advertiser_profile_pic/'),
        ),
        migrations.AlterField(
            model_name='citycorporationprofileinfo',
            name='cityCor_profile_pic',
            field=models.ImageField(blank=True, default='/profiles_pic/cityCor_profile_pic/demo_profile_pic2.png', upload_to='profiles_pic/cityCor_profile_pic'),
        ),
        migrations.AlterField(
            model_name='customerprofileinfo',
            name='Customer_profile_pic',
            field=models.ImageField(blank=True, default='/profiles_pic/Customer_profile_pic/demo_profile_pic2.png', upload_to='profiles_pic/Customer_profile_pic/'),
        ),
        migrations.AlterField(
            model_name='post_advertise_table',
            name='posted_billboards_pic',
            field=models.ImageField(blank=True, default='/posted_billboards_pic/billboards_images/demo_billboard_image.JPG', upload_to='posted_billboards_pic/billboards_images'),
        ),
    ]
