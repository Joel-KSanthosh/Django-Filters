# Generated by Django 5.0.4 on 2024-04-23 06:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GenusModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='SpeciesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ScientificNameModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genus', models.ManyToManyField(related_name='scientifc_genus', to='filters.genusmodel')),
                ('species', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='filters.speciesmodel')),
            ],
        ),
        migrations.CreateModel(
            name='AnimalModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('scientific_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='filters.scientificnamemodel')),
            ],
        ),
    ]
