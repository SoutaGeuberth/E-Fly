# Generated by Django 4.1.7 on 2023-05-26 03:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_vuelo_asientos_fila_vuelo_filas'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=4)),
                ('estado', models.CharField(max_length=20)),
                ('vuelo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='todo.vuelo')),
            ],
        ),
    ]