# Generated by Django 5.0.1 on 2024-02-23 16:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empresas', '0002_perfillocal_nome_estacionamento'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='endereco',
            name='logradouro',
        ),
    ]
