# Generated by Django 4.2.4 on 2023-08-08 05:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('smile_dryApp', '0017_rename_gst_products_feild_1_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ProductsFranchise',
        ),
        migrations.DeleteModel(
            name='StockInFranchise',
        ),
    ]
