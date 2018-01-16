# Generated by Django 2.0.1 on 2018-01-07 07:04

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=200)),
                ('details', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('total', models.IntegerField()),
                ('added_date', models.DateField(default=django.utils.timezone.now)),
                ('added_time', models.TimeField(default=django.utils.timezone.now)),
                ('item_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Item')),
            ],
        ),
    ]