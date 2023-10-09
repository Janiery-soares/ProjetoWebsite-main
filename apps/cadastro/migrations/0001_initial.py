# Generated by Django 4.2.6 on 2023-10-06 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DadosCliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_cliente', models.CharField(max_length=100)),
                ('endereço_cliente', models.TextField()),
                ('complemento_cliente', models.TextField()),
                ('telefone_cliente', models.CharField(max_length=100)),
                ('email_cliente', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='DadosPessoais',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpf', models.CharField(max_length=14)),
                ('rg', models.CharField(max_length=10)),
            ],
        ),
    ]
