# Generated by Django 4.2.4 on 2023-08-11 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smile_dryApp', '0031_remove_franchiseproducts_feild_2_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='feild_1',
        ),
        migrations.AddField(
            model_name='products',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='Products'),
        ),
        migrations.AlterField(
            model_name='franchiseproducts',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='Franchise_Products'),
        ),
    ]
