# Generated by Django 4.2.10 on 2024-02-19 12:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresas', '0004_remove_perfillocal_nota_media'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfillocal',
            name='nota_media',
            field=models.FloatField(blank=True, editable=False, null=True, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(10.0)], verbose_name='nota média'),
        ),
    ]
