# Generated by Django 4.1 on 2022-08-18 19:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=1000, unique=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PlantCategory',
            fields=[
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=1000, unique=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=1000, unique=True)),
                ('scientificName', models.CharField(blank=True, max_length=1000, null=True, unique=True)),
                ('category', models.CharField(blank=True, max_length=1000, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FarmInput',
            fields=[
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=1000, unique=True)),
                ('category', models.CharField(blank=True, max_length=1000, null=True)),
                ('harmful', models.BooleanField(default=False)),
                ('safety_interval', models.IntegerField()),
                ('safety_interval_units', models.CharField(blank=True, max_length=1000, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ActivitySchedule',
            fields=[
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('frequency', models.IntegerField()),
                ('frequency_units', models.CharField(blank=True, max_length=1000, null=True)),
                ('startDate', models.DateTimeField(blank=True, null=True)),
                ('endDate', models.DateTimeField(blank=True, null=True)),
                ('quantity', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('units', models.CharField(blank=True, max_length=1000, null=True)),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.activity')),
                ('plant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.plant')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
