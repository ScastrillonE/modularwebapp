# Generated by Django 3.2.10 on 2021-12-14 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plugin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, verbose_name='Name')),
                ('author', models.CharField(max_length=80, verbose_name='Author')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('installed', models.BooleanField(blank=True, default=False, null=True)),
                ('website', models.CharField(blank=True, max_length=180, null=True, verbose_name='Website')),
                ('color', models.CharField(blank=True, max_length=20, null=True, verbose_name='Color')),
                ('fa', models.CharField(blank=True, max_length=20, null=True, verbose_name='Icon')),
                ('version', models.CharField(blank=True, max_length=20, null=True, verbose_name='Version')),
                ('sequence', models.IntegerField(default=100, verbose_name='Sequence')),
            ],
            options={
                'verbose_name': 'Plugin',
                'verbose_name_plural': 'Plugin',
                'ordering': ['pk'],
            },
        ),
    ]
