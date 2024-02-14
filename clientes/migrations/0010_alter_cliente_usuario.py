# Generated by Django 5.0.1 on 2024-02-09 01:07

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0009_remove_cliente_tipo_usuario_alter_cliente_usuario'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='usuario',
            field=models.ForeignKey(choices=[('ADMIN', 'Admin'), ('CLIENTE', 'Cliente'), ('ESTACIONAMENTO', 'Estacionamento')], default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
