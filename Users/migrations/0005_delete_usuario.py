# Generated by Django 4.2.7 on 2023-12-18 23:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0004_rename_user_usuario_username'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Usuario',
        ),
    ]
