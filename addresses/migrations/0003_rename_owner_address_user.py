# Generated by Django 3.2.25 on 2024-06-21 16:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('addresses', '0002_rename_user_address_owner'),
    ]

    operations = [
        migrations.RenameField(
            model_name='address',
            old_name='owner',
            new_name='user',
        ),
    ]
