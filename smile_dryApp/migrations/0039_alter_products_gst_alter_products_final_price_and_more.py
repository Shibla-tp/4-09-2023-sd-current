# Generated by Django 4.2.4 on 2023-08-12 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smile_dryApp', '0038_alter_products_final_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='GST',
            field=models.FloatField(max_length=100),
        ),
        migrations.AlterField(
            model_name='products',
            name='final_price',
            field=models.FloatField(max_length=10),
        ),
        migrations.AlterField(
            model_name='products',
            name='purchase_rate',
            field=models.FloatField(max_length=100),
        ),
        migrations.AlterField(
            model_name='products',
            name='sale_price',
            field=models.FloatField(max_length=100),
        ),
    ]