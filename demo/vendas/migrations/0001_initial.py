# Generated by Django 5.2 on 2025-04-16 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id_cliente', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=100)),
                ('cpf', models.CharField(max_length=14)),
                ('telefone', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'cliente',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id_pedido', models.AutoField(primary_key=True, serialize=False)),
                ('data_pedido', models.DateField()),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'db_table': 'pedidos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Fornecedor',
            fields=[
                ('id_fornecedor', models.AutoField(primary_key=True, serialize=False)),
                ('nome_fornecedor', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=60)),
                ('telefone_fornecedor', models.CharField(max_length=15)),
            ],
        ),
    ]
