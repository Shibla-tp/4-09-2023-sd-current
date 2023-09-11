# Generated by Django 4.0.4 on 2023-08-04 05:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('smile_dryApp', '0009_delete_laundryproducts'),
    ]

    operations = [
        migrations.CreateModel(
            name='LaundryProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(default=0, max_length=15)),
                ('quantity', models.FloatField(default=0, max_length=15)),
                ('total_amount', models.FloatField(max_length=15)),
                ('pincode', models.CharField(max_length=100)),
                ('feild_2', models.CharField(max_length=100)),
                ('feild_3', models.CharField(max_length=100)),
                ('feild_4', models.CharField(max_length=100)),
                ('feild_5', models.CharField(max_length=100)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_fk', to='smile_dryApp.products')),
                ('productpurchace', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='productpurchace_fk2', to='smile_dryApp.productpurchace')),
            ],
            options={
                'verbose_name_plural': 'List of Laundry Products',
            },
        ),
    ]
