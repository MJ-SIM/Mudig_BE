# Generated by Django 4.2.7 on 2023-11-16 10:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='genre',
            new_name='gnere',
        ),
    ]
