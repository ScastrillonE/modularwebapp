# Generated by Django 3.2.10 on 2021-12-14 03:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'Person', 'verbose_name_plural': 'People'},
        ),
        migrations.AlterModelTable(
            name='user',
            table='auth_user',
        ),
    ]
