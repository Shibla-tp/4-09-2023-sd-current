# Generated by Django 4.2.4 on 2023-08-12 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smile_dryApp', '0037_rename_feild_2_products_gst_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='final_price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
