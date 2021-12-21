# Generated by Django 3.2.10 on 2021-12-14 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_auto_20211214_0443'),
    ]

    operations = [
        migrations.RenameField(
            model_name='plugin',
            old_name='fa',
            new_name='icon',
        ),
        migrations.AddField(
            model_name='plugin',
            name='category',
            field=models.CharField(default=0, max_length=80, verbose_name='Category'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='plugin',
            name='installable',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
