# Generated by Django 3.2.4 on 2021-06-16 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0005_vendor_disable'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vendor',
            name='disable',
        ),
        migrations.AddField(
            model_name='vendor',
            name='enabled',
            field=models.BooleanField(default=True),
        ),
    ]
