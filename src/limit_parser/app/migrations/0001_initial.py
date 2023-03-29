# Generated by Django 4.1.7 on 2023-03-29 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FuelCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=16)),
                ('is_took', models.BooleanField(default='False')),
                ('has_limit', models.BooleanField(default='False')),
                ('took_time', models.TimeField(blank=True, null=True)),
                ('changed_time', models.TimeField(blank=True, null=True)),
            ],
        ),
    ]
