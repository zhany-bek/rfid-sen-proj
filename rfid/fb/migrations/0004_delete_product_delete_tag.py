# Generated by Django 4.2.7 on 2023-11-12 16:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fb', '0003_product'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]