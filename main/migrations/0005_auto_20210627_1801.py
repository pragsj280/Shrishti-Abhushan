# Generated by Django 3.1.6 on 2021-06-27 12:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_remove_customer_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='locality',
            new_name='address',
        ),
    ]
