# Generated by Django 4.2.4 on 2023-08-08 16:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('smile_dryApp', '0024_delete_franchiselaundryproducts'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='franchisestockin',
            name='franchiseproduct',
        ),
        migrations.DeleteModel(
            name='FranchiseProducts',
        ),
        migrations.DeleteModel(
            name='FranchiseStockIn',
        ),
    ]
