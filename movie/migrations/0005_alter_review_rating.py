# Generated by Django 5.1.4 on 2024-12-14 15:08

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0004_alter_review_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.IntegerField(choices=[(1, 'Very Poor'), (2, 'Poor'), (3, 'Average'), (4, 'Good'), (5, 'Excellent')], validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(5.0)]),
        ),
    ]
