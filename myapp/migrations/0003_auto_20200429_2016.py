# Generated by Django 3.0.2 on 2020-04-29 20:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_attendace'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='attendace',
            new_name='attendance',
        ),
    ]