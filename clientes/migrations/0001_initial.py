# Generated by Django 5.0.1 on 2024-01-26 14:45

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('empresas', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('sobrenome', models.CharField(max_length=150)),
                ('data_nasc', models.DateField(verbose_name='data de nascimento')),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='Avaliacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('critica', models.CharField(max_length=1000, null=True, verbose_name='crítica')),
                ('data_envio', models.DateTimeField(auto_now_add=True, verbose_name='data de envio')),
                ('nota', models.DecimalField(decimal_places=1, max_digits=3, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
                ('avaliado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='estacionamento_avaliado', to='empresas.estacionamento', verbose_name='avaliado')),
                ('avaliador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cliente_avaliador', to='clientes.cliente', verbose_name='avaliador')),
            ],
            options={
                'verbose_name': 'avaliação de usuários',
                'verbose_name_plural': 'avaliações de usuários',
                'ordering': ['data_envio'],
            },
        ),
    ]
