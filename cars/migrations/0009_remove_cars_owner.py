# Generated by Django 4.2.5 on 2023-10-05 01:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0008_alter_cars_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cars',
            name='owner',
        ),
    ]