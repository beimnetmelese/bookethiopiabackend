# Generated by Django 5.1.2 on 2024-11-02 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0003_room_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='descriptions',
            field=models.TextField(blank=True, null=True),
        ),
    ]
