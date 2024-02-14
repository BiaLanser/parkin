# Generated by Django 5.0.1 on 2024-02-06 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresas', '0012_alter_perfillocal_dias_abertos'),
    ]

    operations = [
        migrations.CreateModel(
            name='Opcao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Selecao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opcoes', models.ManyToManyField(to='empresas.opcao')),
            ],
        ),
    ]