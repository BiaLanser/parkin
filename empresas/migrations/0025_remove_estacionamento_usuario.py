# Generated by Django 5.0.1 on 2024-02-09 03:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empresas', '0024_alter_estacionamento_usuario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estacionamento',
            name='usuario',
        ),
    ]