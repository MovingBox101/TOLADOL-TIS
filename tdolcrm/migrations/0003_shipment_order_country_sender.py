# Generated by Django 4.1.6 on 2023-06-15 16:37

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('tdolcrm', '0002_shipment_order_country_shipment_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='shipment_order',
            name='Country_sender',
            field=django_countries.fields.CountryField(default='', max_length=2, verbose_name='Country'),
        ),
    ]
