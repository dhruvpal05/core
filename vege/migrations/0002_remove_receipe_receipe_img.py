# Generated by Django 4.2.5 on 2023-10-06 13:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vege', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='receipe',
            name='receipe_img',
        ),
    ]
