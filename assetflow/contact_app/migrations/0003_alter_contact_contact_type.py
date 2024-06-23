# Generated by Django 4.2.13 on 2024-06-23 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_app', '0002_alter_contact_contact_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='contact_type',
            field=models.CharField(choices=[('seller', 'Seller'), ('buyer', 'Buyer'), ('both', 'Both')], default='Both', max_length=10),
        ),
    ]
