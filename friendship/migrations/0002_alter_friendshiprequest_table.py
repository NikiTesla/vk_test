# Generated by Django 3.2.18 on 2023-05-06 14:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('friendship', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='friendshiprequest',
            table='friendship_requests',
        ),
    ]
