# Generated by Django 4.1.6 on 2023-06-21 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tdolcrm', '0004_shipment_order_postal_code_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='shipment_order',
            name='Height',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='shipment_order',
            name='Total_weight',
            field=models.IntegerField(default=0, verbose_name='Total Weight'),
        ),
        migrations.AddField(
            model_name='shipment_order',
            name='Weight',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='shipment_order',
            name='length',
            field=models.IntegerField(default=0),
        ),
    ]
