# Generated by Django 5.1.2 on 2024-11-21 13:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='hotel',
        ),
    ]
