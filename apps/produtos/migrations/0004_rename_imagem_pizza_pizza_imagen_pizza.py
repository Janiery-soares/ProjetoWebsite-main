# Generated by Django 4.2.6 on 2023-10-31 11:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0003_alter_pizza_sabor_pizza'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pizza',
            old_name='imagem_pizza',
            new_name='imagen_pizza',
        ),
    ]
