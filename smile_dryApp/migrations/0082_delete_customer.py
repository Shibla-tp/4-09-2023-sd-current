# Generated by Django 4.2.4 on 2023-09-06 07:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('smile_dryApp', '0081_alter_coupon_franchise_details'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Customer',
        ),
    ]