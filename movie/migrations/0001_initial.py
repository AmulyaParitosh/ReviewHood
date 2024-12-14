# Generated by Django 5.1.4 on 2024-12-14 10:45

import django.core.validators
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=127, unique=True)),
                ('age', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('others', 'Others')], max_length=7)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=127, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=127, unique=True)),
                ('rating', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(5.0)])),
                ('release_date', models.DateField()),
                ('actors', models.ManyToManyField(related_name='movies', to='movie.actor')),
                ('genres', models.ManyToManyField(related_name='movies', to='movie.genre')),
            ],
        ),
    ]