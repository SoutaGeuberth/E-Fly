# Generated by Django 4.1.7 on 2023-05-23 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0005_alter_vuelo_codigo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vuelo',
            name='horaLlegada',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='vuelo',
            name='horaSalida',
            field=models.DateTimeField(),
        ),
    ]
