# Generated by Django 3.2 on 2021-06-14 17:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0003_remove_cartitem_variations'),
        ('store', '0002_variation'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Variation',
        ),
    ]
