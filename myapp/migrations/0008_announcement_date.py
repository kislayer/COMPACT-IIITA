# Generated by Django 3.0.2 on 2020-05-01 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_announcement'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcement',
            name='Date',
            field=models.CharField(default='DEFAULT VALUE', max_length=20),
        ),
    ]