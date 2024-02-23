# Generated by Django 5.0.1 on 2024-02-23 17:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresas', '0006_alter_perfillocal_endereco'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfillocal',
            name='endereco',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='endereco_perfil', to='empresas.endereco'),
        ),
    ]
