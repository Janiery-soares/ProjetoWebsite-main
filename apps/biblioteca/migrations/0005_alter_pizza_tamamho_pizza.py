# Generated by Django 4.2.6 on 2023-10-06 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0004_alter_pizza_borda_pizza_alter_pizza_tamamho_pizza'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizza',
            name='tamamho_pizza',
            field=models.CharField(choices=[('F', 'Família'), ('B', 'Brotinho'), ('p', 'pequena'), ('G', 'Grande'), ('M', 'Média')], max_length=1),
        ),
    ]
