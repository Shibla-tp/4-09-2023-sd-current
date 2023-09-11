# Generated by Django 4.2.4 on 2023-08-12 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smile_dryApp', '0039_alter_products_gst_alter_products_final_price_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='price',
        ),
        migrations.AddField(
            model_name='products',
            name='total_purchase_rate',
            field=models.FloatField(default=0, max_length=10),
        ),
        migrations.AlterField(
            model_name='products',
            name='final_price',
            field=models.FloatField(default=0, max_length=15),
        ),
    ]