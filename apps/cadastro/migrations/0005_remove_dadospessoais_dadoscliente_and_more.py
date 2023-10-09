# Generated by Django 4.2.6 on 2023-10-06 23:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0009_rename_add_pedido_pedido_adicionar_pedido'),
        ('cadastro', '0004_remove_dadoscliente_pedido'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dadospessoais',
            name='dadoscliente',
        ),
        migrations.AddField(
            model_name='dadoscliente',
            name='pedido',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='biblioteca.pedido'),
            preserve_default=False,
        ),
    ]
