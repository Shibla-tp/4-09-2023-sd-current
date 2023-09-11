# Generated by Django 4.2.4 on 2023-09-02 09:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('smile_dryApp', '0073_staffs_aadhar_staffs_pan_card_staffs_photo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coupon',
            old_name='Franchise_name',
            new_name='franchise_details',
        ),
        migrations.AlterField(
            model_name='franchiseproducts',
            name='franchise_details',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]