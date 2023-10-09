# Generated by Django 4.2.6 on 2023-10-07 00:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0011_pedido'),
        ('cadastro', '0006_remove_dadoscliente_pedido'),
    ]

    operations = [
        migrations.AddField(
            model_name='dadoscliente',
            name='pedido',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='biblioteca.pedido'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dadospessoais',
            name='dadoscliente',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='cadastro.dadoscliente'),
            preserve_default=False,
        ),
    ]
