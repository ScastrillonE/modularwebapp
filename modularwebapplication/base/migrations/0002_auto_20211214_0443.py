# Generated by Django 3.2.10 on 2021-12-14 04:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plugin',
            name='sequence',
        ),
        migrations.RemoveField(
            model_name='plugin',
            name='website',
        ),
    ]