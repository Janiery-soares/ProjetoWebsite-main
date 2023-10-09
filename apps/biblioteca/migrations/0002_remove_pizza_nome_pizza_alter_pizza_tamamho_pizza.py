# Generated by Django 4.2.6 on 2023-10-06 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pizza',
            name='nome_pizza',
        ),
        migrations.AlterField(
            model_name='pizza',
            name='tamamho_pizza',
            field=models.CharField(choices=[('F', 'Família'), ('G', 'Grande'), ('M', 'Média'), ('B', 'Brotinho'), ('p', 'pequena')], max_length=1),
        ),
    ]
